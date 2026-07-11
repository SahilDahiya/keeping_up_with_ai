---
title: SDXL inference in under 2 seconds
topic: inference
subtopic: optimization
secondary_topics:
- models/multimodal
summary: Guide to Stable Diffusion XL inference optimization for sub-2-second image
  generation.
source: baseten
url: https://www.baseten.co/blog/sdxl-inference-in-under-2-seconds-the-ultimate-guide-to-stable-diffusion-optimiza/
author: Varun Shenoy; Philip Kiely
published: '2023-08-30'
fetched: '2026-07-11T04:10:44Z'
classifier: codex
taxonomy_rev: 1
words: 1514
content_sha256: d82e9325576444c95dcde085c4f73ea5f35dadb2e241395211925803d1f4faa4
triage: keep
skip_reason: null
---

# SDXL inference in under 2 seconds

![SDXL in under 2 seconds](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1747610222-sdxl-2s.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

Out of the box, [Stable Diffusion XL 1.0 (SDXL)](https://www.baseten.co/library/stable-diffusion-xl/) takes 8-10 seconds to create a 1024x1024px image from a prompt on an A100 GPU. But I couldn’t wait that long to see a picture of “a man in a space suit playing a guitar.” So I set out to speed up model inference for Stable Diffusion.

Author's note: we've [made SDXL inference even faster with TensorRT and H100 GPUs](https://www.baseten.co/blog/40-faster-stable-diffusion-xl-inference-with-nvidia-tensorrt/).

There’s no one universal tactic for optimizing all model inference. Instead, it’s more like squeezing the most speed out of a racecar: making a bunch of tweaks that work together for maximum performance. Here’s everything I did to cut SDXL invocation to as fast as 1.92 seconds on an A100:

- Cut the number of steps from 50 to 20 with minimal impact on results quality.
- Set classifier free guidance (CFG) to zero after 8 steps.
- Swapped in the refiner model for the last 20% of the steps.
- Used - `torch.compile`to optimize the model for an A100 GPU.
- Chose a fp16 vae and efficient attention to improve memory efficiency.

The last step also unlocks major cost efficiency by making it possible to run SDXL on the cheapest A10G instance type. The optimized model runs in just 4-6 seconds on an A10G, and at ⅕ the cost of an A100, that’s substantial savings for a wide variety of use cases.

![Stable Diffusion inference logs](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842620-64efd4031a396db73736d12c_vdsplprtkptb0o2qggdav3smt9jbd0r2xwcuq5z0zfewu_lwson57auxwm9shkyxjw33lvt79qlhuojwu2vuilaagusn1_sufw1akvfrfgts4mhi8vki2wlei8xa9hjlbf1vwt1esw3zyq8adfn3ypq.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Stable Diffusion inference logs

Stable Diffusion inference logsIf you want to use this optimized version of SDXL, you can [deploy it in two clicks from the model library](https://www.baseten.co/library/stable-diffusion-xl/). Network latency can add a second or two to the time it takes to receive a finished image, so check the model logs for invocation-only benchmarks.

## Cut from 50 to 20 steps

Optimization is about tradeoffs. In this case, I’m trading off between generation speed and image quality. The trick is finding places where those tradeoffs are possible, then experimenting to find where you can get a lot of marginal speed by sacrificing little to no marginal quality.

The biggest speed-up possible comes from limiting the number of steps that the model takes to generate the image. A diffusion model starts with an image that’s just noise and iterates toward the final output. Inference time scales linearly with the number of iterations.

But the quality of the resulting image is not linear. Earlier steps have much more impact than later ones.

![Quality increases logarithmically with step count](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842656-64efd403d0f97056e830b7e3_t3m3mjrk36nprweltipogo1snql2vvud1t3pfsx92l8kkpfy_ajo6faa-jplpn_fxc02pbd_gfgj7sbpvsz-kfncnm09djfocqyzszu2ks9xecrivak9qddmzn5eer4pt3qeejopjizm_bl2ius8x8u.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Quality increases logarithmically with step count

Quality increases logarithmically with step countSo to reduce inference time, the first place I looked was to see if I could sacrifice imperceptible gains in results quality for huge speed-ups in inference time. It turns out that the default number of steps for SDXL is 50, which leaves a lot of room to cut.

The question is where the marginal gains on image quality start to flatten out. After experimentation and research, I found that 20 steps was just enough to create very high-quality images.

![50 steps of SDXL in 7.08s](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842323-64efd404b46aca3459025749_fijec65xg_4unnv9kh_upudofmp0zwo37aobedcbqzz5q0lu6uy5nn-bm8fpjlbtsbem8kymrm52n2mdaarhzfihxybjzmnejthy89la2lawcx3kadmdeir0ck4auccgysnxqdgdn732tklcixbfpim.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) 50 steps of SDXL in 7.08s

50 steps of SDXL in 7.08s## Set CFG to zero after 40% of steps

*A big thanks to **Erwann Millon** for giving me this tip when he stopped by the Baseten office.*

[Classifier Free Guidance](https://arxiv.org/abs/2207.12598) (CFG) is a parameter that adjusts how closely the model output matches the prompt. It’s not dissimilar to temperature for an LLM, though in this case a higher CFG means a stricter adherence to the prompt.

The tradeoff for this increased accuracy is that using any amount of CFG doubles the batch size of each step, which slows down invocation.

![The code in diffusors to add end_cfg](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842700-64efd403ccec40ab6445e8ba_5jwd_jo8shom53ezcourgpf3gsnvfgseot8xee1uonvxb0wv8m9n9xp68lrsgycfvh60unamevrxxp1paxvhqhp1ak7m1g33w3zsfdkws03qdozi2ki7eswqtnanzye88pw4hvd-0sz7ramznr2qa4.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The code in diffusors to add end_cfg

The code in diffusors to add end_cfgTaking a step back, Stable Diffusion goes from noise to a final image. At some point in that process, the main features of the image are set. The details of the image depend less on the prompt and more on the model’s underlying ability to construct realistic and coherent images.

So, partway through the invocation, I can stop using CFG by setting it to zero. This way, the prompt still has extra influence on the essential first steps of generating an image, and the later steps where it is not as useful are faster for its absence. Per my testing, turning the CFG off after 40% of the steps was the right tradeoff between marginal speed and marginal image quality. I forked Hugging Face’s Diffusers library to add `end_cfg` as a parameter.

![Images and generation times with cfg, without cfg, and with partial cfg](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842727-64efd403830932c72c6374ac_7jxickeypagnra5ksvknxfigqzcbjgzjlj4za26hbqmtjrdjcbf9jx6yghvnqqounbfv45e1wolmqwt1d04jyfhy9bk0sgqwpa9wgcquechprzgcorldrauw-ptafhcl-gcpghjpuzjz6-lycivvxa.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) Images and generation times with cfg, without cfg, and with partial cfg

Images and generation times with cfg, without cfg, and with partial cfg## Switch to refiner model for final 20%

SDXL has an optional refiner model that can take the output of the base model and modify details to improve accuracy around things like hands and faces that often get messed up. This adds to the inference time because it requires extra inference steps.

However, the last few inference steps are all about details anyway. So rather than taking the time to fill all of the details in, then passing the output to the refiner model to have those details re-done, I instead use the refiner model for the final 20% of inference steps.

![The last 20% of the steps use the refiner model](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842620-64efd4031a396db73736d12c_vdsplprtkptb0o2qggdav3smt9jbd0r2xwcuq5z0zfewu_lwson57auxwm9shkyxjw33lvt79qlhuojwu2vuilaagusn1_sufw1akvfrfgts4mhi8vki2wlei8xa9hjlbf1vwt1esw3zyq8adfn3ypq.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) The last 20% of the steps use the refiner model

The last 20% of the steps use the refiner model## Compile the model to take advantage of A100s

The last step I took was to use `torch.compile` with the `max-autotune` configuration to automatically compile the base and refiner models to run efficiently on our hardware of choice. The max autotune argument guarantees that `torch.compile` finds the fastest optimizations for SDXL. This comes with the drawback of a long just-in-time (JIT) compilation time on the first inference (around 40 minutes), so it’s not included in the optimized version of SDXL in the model library.

More specifically, `torch.compile` with max autotune will:

- Profile the model with different optimization configurations (like tensor fusion, operator fusion, etc.)
- Run a large search over possible optimizations and select the best performing configuration
- Generate optimized machine code for the model using the best found configuration

In summary, `torch.compile` with max autotune spends more time profiling and tuning the model compared to the default behavior, in order to find the optimal compilation settings for maximizing inference performance. This works well for models where you want to get the absolute best performance, without regard for compile time.

With model compilation, I achieved a model inference of 1.92s with 20 steps on an A100.

![SDXL inference time with and without max autotune](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1693842810-64efd40383bd586b5fef7326_kmcpklzariz7ezhi-awupekagyln0mjrqxq4qry1m1cxoiryoyv9t1klqfz0dqoztirwqnqvvgumbhngehzzm8sdqftfhqvm5dx79dbazgm-qc-xp8uebslwdmhf-pcpst_vbnny7wwzya2lmecegb0.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75) SDXL inference time with and without max autotune

SDXL inference time with and without max autotune## Use fp16 vae and efficient attention

By default, models run at floating point 32 (fp32) precision on GPUs, meaning they do calculations with 32 significant figures of precision. Quantizing a model means running its calculations at a lower precision. This means each calculation takes less time and VRAM. Higher precision can improve model output, but most popular generative models run very well at half that precision (fp16), and often even lower precisions.

When SDXL was released, the model came in both fp32 and a quantized fp16 version, but its variational autoencoder (vae) was fp32-only. This meant some calculations had to be run in fp32, increasing inference time and VRAM requirements.

I used a[ community-built fp16 vae](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix) alongside the fp16 version of Stable Diffusion to ensure the entire image generation sequence ran the faster, more memory efficient float-16 precision. This has no discernible impact on model quality.

I also used an efficient attention implementation from xformers. Alongside the fp16 vae, this ensures that SDXL runs on the smallest available A10G instance type. And thanks to the other optimizations, it actually runs faster on an A10 than the un-optimized version did on an A100. You can expect inference times of 4 to 6 seconds on an A10.

## Get started with SDXL

Through experimentation and research, I was able to speed up SDXL invocation by a factor of four by reducing the number of inference steps while balancing results quality then using CFG and the refiner model only on the steps where they have the highest impact and reducing the memory needs of the model with an fp16 vae and efficient attention.

I also applied all these optimizations to standard Stable Diffusion, achieving generation times of under a second on an A10G and under half a second on an A100.

But you can skip all of that work and go straight to generating images fast with SDXL:

- [Deploy SDXL on an A10](https://www.baseten.co/library/stable-diffusion-xl/)from the model library for 6 second inference times.
- For even faster inference, try - [Stable Diffusion 1.5](https://www.baseten.co/library/stable-diffusion/)and get 20-step images in less than a second.
- Check out the optimizations to SDXL for yourself - [on GitHub](https://github.com/basetenlabs/truss-examples/tree/main/stable-diffusion/stable-diffusion-xl-1.0).
