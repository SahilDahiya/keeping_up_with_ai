---
title: Canopy Labs selects Baseten as preferred inference provider for Orpheus TTS
  models
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/canopy-labs-selects-baseten-as-preferred-inference-provider-for-orpheus-tts-model
author: Philip Kiely
published: '2025-05-05'
fetched: '2026-11-12T06:09:58Z'
classifier: null
taxonomy_rev: 2
words: 1226
content_sha256: ed2b6918f59a70c5bc3655559874ec2419500eae6eca4c959acacce7002b3bb0
---

# Canopy Labs selects Baseten as preferred inference provider for Orpheus TTS models

Community
# Canopy Labs selects Baseten as preferred inference provider for Orpheus TTS models

Canopy Labs recommends that startups run Orpheus TTS, their open source speech synthesis model, on Baseten for production


- Authors
- Date
- May 5, 2025

[Canopy Labs](https://canopylabs.ai/), a foundation model company operating in San Francisco, is on a mission to build digital humans that are indistinguishable from real humans. In March, they released [Orpheus TTS](https://www.baseten.co/library/orpheus-tts/), an open-source model for real-time lifelike speech synthesis.

Orpheus went viral, racking up over 100K downloads on Hugging Face as a top 5 trending model. As thousands of developers experimented with Orpheus, many began to ask how to run the model in production.

To help developers use Orpheus TTS in production, Canopy Labs has selected Baseten as its preferred inference provider. Baseten and Canopy have collaborated to create the world’s [highest-performance Orpheus inference server](https://github.com/basetenlabs/truss-examples/tree/main/orpheus-best-performance) based on NVIDIA’s TensorRT-LLM.

We’re excited to partner with Baseten to optimize and serve Orpheus TTS for demanding AI applications like real-time voice agents.


Below, we’ll dive into benchmarks, optimizations, and client code for Orpheus on Baseten. You can [deploy the model in a couple of clicks](https://www.baseten.co/library/orpheus-tts/) from Baseten’s model library to get started building with Orpheus instantly.

Benchmarking performance for TTS models is interesting because you’re not as concerned with raw tokens per second as with LLMs. For Orpheus, 83 tokens is roughly equivalent to one second of audio. So once you can get to 83 tokens per second, you actually want to increase batch size rather than token speed to support more real-time connections on the same hardware, reducing cost.

Our original implementation of Orpheus supported 7 simultaneous real-time streams on an H100 MIG GPU – effectively half of an H100 for cost-efficient performance. After optimizing the model with TensorRT-LLM, we see a base rate of 16 simultaneous streams or up to 24 for applications with stable traffic patterns.

The other key metric to optimize for is time to first byte (TTFB). The first byte of response in streaming output gives users the sense of instant response. Baseten’s Orpheus implementation achieves the gold standard of a 200-millisecond TTFB on H100 MIG, equal to the average human reaction time. On a full H100, we get below 150 milliseconds.

There are also non real-time use cases for Orpheus, like generating podcasts, audiobooks, YouTube videos, and more. In these cases, cost-efficient throughput is more important than individual request latency. By increasing the batch size as high as 128 concurrent requests, you can double your token throughput for latency-insensitive tasks, effectively cutting costs in half again.

How did we achieve these performance outcomes? The key strategy was applying LLM-specific tooling to a new modality.

Orpheus TTS is based on the Llama 3.2 3B model, a familiar architecture for Baseten’s model performance tooling. Using the [TensorRT-LLM Engine Builder](https://www.baseten.co/blog/automatic-llm-optimization-with-tensorrt-llm-engine-builder/), we were able to apply multiple optimizations, including FP8 quantization, chunked context, and llama-specific CUDA optimizations to improve performance.

We selected the H100 MIG GPU as the best hardware option for cost-efficient Orpheus inference. An H100 MIG is essentially half of an H100 GPU, with 40 GB of VRAM and 3/7 compute partitions. With its Hopper architecture, H100 MIGs offer [excellent performance with TensorRT-LLM](https://www.baseten.co/blog/using-fractional-h100-gpus-for-efficient-model-serving/) and support [efficient FP8 quantization](https://www.baseten.co/blog/33-faster-llm-inference-with-fp8-quantization/).

As Orpheus is such a small model, with only three billion parameters, the MIG’s reduced VRAM is still more than enough to hold model weights and run large batches. While the full H100 may offer marginally better performance, for these workloads it makes more sense to split the GPU in half and replicate across each half independently.

Calling speech synthesis models, especially in real-time applications, is not as standardized as other modalities. But client code is essential for high-performance voice agents, in fact, it’s not uncommon for subtle errors in model calling to add hundreds of milliseconds of latency.

We’ve written some sample client code designed to get you started and avoid common pitfalls.

python

```
import asyncio
import aiohttp
import uuid
import time
import os
from concurrent.futures import ProcessPoolExecutor
# Configuration
MODEL = "abcd1234"
BASETEN_HOST = f"https://model-{MODEL}.api.baseten.co/environments/production/predict"
BASETEN_API_KEY = os.environ["BASETEN_API_KEY"]
PAYLOADS_PER_PROCESS = 5000
NUM_PROCESSES = 8
MAX_REQUESTS_PER_PROCESS = 1
# Sample prompts
prompts = [
    """Hello there.
Thank you for calling our support line.
My name is Sarah and I'll be helping you today.
Could you please provide your account number and tell me what issue you're experiencing?"""
]
prompt_types = ["short", "medium", "long"]
base_request_payload = {
    "max_tokens": 4096,
    "voice": "tara",
    "stop_token_ids": [128258, 128009],
}
async def stream_to_buffer(
    session: aiohttp.ClientSession, label: str, payload: dict
) -> bytes:
    """Send one streaming request, accumulate into bytes, and log timings."""
    req_id = str(uuid.uuid4())
    payload = {**payload, "request_id": req_id}
    t0 = time.perf_counter()
    try:
        async with session.post(
            BASETEN_HOST,
            json=payload,
            headers={"Authorization": f"Api-Key {BASETEN_API_KEY}"},
        ) as resp:
            if resp.status != 200:
                print(f"[{label}] ← HTTP {resp.status}")
                return b""
            buf = bytearray()
            idx = 0
            # *** CORRECTED: async for on the AsyncStreamIterator ***
            async for chunk in resp.content.iter_chunked(4_096):
                elapsed_ms = (time.perf_counter() - t0) * 1_000
                if idx in [0]:
                    print(
                        f"[{label}] ← chunk#{idx} ({len(chunk)} B) @ {elapsed_ms:.1f} ms"
                    )
                buf.extend(chunk)
                idx += 1
            total_s = time.perf_counter() - t0
            print(f"[{label}] ← done {len(buf)} B in {total_s:.2f}s")
            return bytes(buf)
    except Exception as e:
        print(f"[{label}] ⚠️ exception: {e!r}")
        return b""
async def run_session(
    session: aiohttp.ClientSession,
    prompt: str,
    ptype: str,
    run_id: int,
    semaphore: asyncio.Semaphore,
) -> None:
    """Wrap a single prompt run in its own error‐safe block."""
    label = f"{ptype}_run{run_id}"
    async with semaphore:
        try:
            payload = {**base_request_payload, "prompt": f"Chapter {run_id}: {prompt}"}
            buf = await stream_to_buffer(session, label, payload)
            if run_id < 3 and buf:
                fn = f"output_{ptype}_run{run_id}.wav"
                with open(fn, "wb") as f:
                    f.write(buf)
                print(f"[{label}] ➔ saved {fn}")
        except Exception as e:
            print(f"[{label}] 🛑 failed: {e!r}")
async def run_with_offset(offset: int) -> None:
    semph = asyncio.Semaphore(MAX_REQUESTS_PER_PROCESS)
    connector = aiohttp.TCPConnector(limit_per_host=128, limit=128)
    async with aiohttp.ClientSession(connector=connector) as session:
        # warmup once per worker
        await run_session(session, "warmup", "warmup", 90 + offset, semph)
        tasks = []
        for i, prompt in enumerate(prompts):
            ptype = prompt_types[i]
            print(f"\nWorker@offset {offset} ▶ {ptype} prompt starts…")
            for run_id in range(offset, offset + PAYLOADS_PER_PROCESS):
                tasks.append(run_session(session, prompt, ptype, run_id, semph))
        await asyncio.gather(*tasks)
        print(f"Worker@offset {offset} ✅ all done.")
def run_with_offset_sync(offset: int) -> None:
    try:
        # create and run a fresh event loop in each process
        asyncio.run(run_with_offset(offset))
    except Exception as e:
        print(f"Worker@offset {offset} ❌ error: {e}")
def main():
    offsets = [i * PAYLOADS_PER_PROCESS for i in range(NUM_PROCESSES)]
    with ProcessPoolExecutor() as exe:
        # map each offset to its own process
        exe.map(run_with_offset_sync, offsets)
    print("🎉 All processes completed.")
if __name__ == "__main__":
    main()
```
One key aspect of this client code is session re-use. Establishing a session introduces overhead – sometimes as much as a hundred milliseconds – substantially impacting observed TTFB performance. With session re-use, the vast majority of requests skip this bottleneck and run with the expected latency.

For more details on calling Orpheus, check out our [sample code](https://github.com/canopyai/Orpheus-TTS/tree/main/additional_inference_options/baseten_inference_example) in the Orpheus TTS repo.

Canopy Labs chose Baseten as its preferred inference platform for Orpheus TTS thanks to Baseten’s TensorRT-LLM model performance optimizations, scalable infrastructure, and feature-rich model management tooling.

On a single H100 MIG, you can run Orpheus with:

- 16 concurrent live connections with variable traffic
- 24 concurrent live connections with stable traffic
- Up to 60x real-time factor for bulk jobs

Orpheus TTS is a fast, configurable, cost-efficient option for speech synthesis for large-scale voice agents. You can get started building with Orpheus with a [pre-optimized model library deployment](https://www.baseten.co/library/orpheus-tts/) and the [client code example](https://github.com/canopyai/Orpheus-TTS/tree/main/additional_inference_options/baseten_inference_example).
