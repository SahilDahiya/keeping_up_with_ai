---
title: Make your ZeroGPU Spaces go brrr with ahead-of-time compilation
kind: blog
topic: inference
subtopic: kernels
secondary_topics:
- infra-platform/deployment
summary: Uses PyTorch ahead-of-time compilation (torch.export + AOTInductor) instead
  of just-in-time torch.compile so short-lived ZeroGPU processes keep the compiled
  artifact, giving 1.3x-1.8x speedups on Flux, Wan and LTX; also covers FP8 quantization,
  dynamic shapes and multi-compile for varying resolutions.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/zerogpu-aoti
author: Charles Bensimon; Sayak Paul; Linoy Tsaban; Apolinário
published: '2025-09-02'
fetched: '2026-07-14T22:05:18Z'
classifier: claude
taxonomy_rev: 1
words: 2603
content_sha256: 563da19cedf093700ff049540aa4d06eda39d26b51a4b512f6ac3c7c38f980c5
---

# Make your ZeroGPU Spaces go brrr with ahead-of-time compilation

Updated   •  42k  •  43  

#### kernels-community/vllm-flash-attn3

![](https://cdn-avatars.huggingface.co/v1/production/uploads/6452d5ba3f80ad88c77b2f05/0J-xey5Z1dh9ZOyTyyTge.png) 

 Published
					September 2, 2025 

  Upvote 

 80

This is where PyTorch ahead-of-time (AoT) compilation comes in. Instead of compiling models on the fly (which doesn’t play nicely with ZeroGPU’s short-lived processes), AoT lets you optimize once and reload instantly.

**The result**: snappier demos and a smoother experience, with speedups ranging from **1.3×–1.8×** on models like Flux, Wan, and LTX 🔥

In this post, we’ll show how to wire up Ahead-of-Time (AoT) compilation in ZeroGPU Spaces. We'll explore advanced tricks like FP8 quantization and dynamic shapes, and share working demos you can try right away. If you cannot wait, we invite you to check out some ZeroGPU-powered demos on the [zerogpu-aoti](https://huggingface.co/zerogpu-aoti) organization.


[Pro](https://huggingface.co/pro)users and[Team / Enterprise](https://huggingface.co/enterprise)org members can create ZeroGPU Spaces, while anyone can freely use them (Pro, Team and Enterprise users get8xmore ZeroGPU quota)

- [What is ZeroGPU](https://huggingface.co#what-is-zerogpu)
- [PyTorch compilation](https://huggingface.co#pytorch-compilation)
- [Ahead-of-time compilation on ZeroGPU](https://huggingface.co#ahead-of-time-compilation-on-zerogpu)
- [Gotchas](https://huggingface.co#gotchas)
- [AoT compiled ZeroGPU Spaces demos](https://huggingface.co#aot-compiled-zerogpu-spaces-demos)
- [Conclusion](https://huggingface.co#conclusion)
- [Resources](https://huggingface.co#resources)

[Spaces](https://huggingface.co/spaces) is a platform powered by Hugging Face that allows ML practitioners to easily publish demo apps.

Typical demo apps on Spaces look like:

```
import gradio as gr
from diffusers import DiffusionPipeline
pipe = DiffusionPipeline.from_pretrained(...).to('cuda')
def generate(prompt):
    return pipe(prompt).images
gr.Interface(generate, "text", "gallery").launch()
```
This works great, but ends up reserving a GPU for the Space during its entire lifetime – even when it has no user activity.

When executing `.to('cuda')` on this line:

```
pipe = DiffusionPipeline.from_pretrained(...).to('cuda')
```
PyTorch initializes the NVIDIA driver, which sets up the process on CUDA forever. This is not very resource-efficient given that app traffic is not perfectly smooth, but is rather extremely sparse and spiky.

ZeroGPU takes a just-in-time approach to GPU initialization. Instead of setting up the main process on CUDA, it automatically forks the process, sets it up on CUDA, runs the GPU tasks, and finally kills the fork when the GPU needs to be released.

This means that:

- When the app does not receive traffic, it doesn't use any GPU
- When it is actually performing a task, it will use one GPU
- It can use multiple GPUs as needed to perform tasks concurrently

Thanks to the Python `spaces` package, the only code change needed to get this behaviour is as follows:

```
  import gradio as gr
+ import spaces
  from diffusers import DiffusionPipeline
  pipe = DiffusionPipeline.from_pretrained(...).to('cuda')
+ @spaces.GPU
  def generate(prompt):
      return pipe(prompt).images
  gr.Interface(generate, "text", "gallery").launch()
```
By importing `spaces` and adding the `@spaces.GPU` decorator, we:

- Intercept PyTorch API calls to postpone CUDA operations
- Make the decorated function run in a fork when later called
- (Call an internal API to make the right device visible to the fork but this is not in the scope of this blogpost)

ZeroGPU currently allocates an

[MIG](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#h200-mig-profiles)slice of H200 (`3g.71gb`profile). Additional MIG sizes including full slice (`7g.141gb`profile) will come in late 2025.

Modern ML frameworks like PyTorch and JAX have the concept of *compilation* that can be used to optimize model latency or inference time. Behind the scenes, compilation applies a series of (often hardware-dependent) optimization steps such as operator fusion, constant folding, etc.

PyTorch (from 2.0 onwards) currently has two major interfaces for compilation:

- Just-in-time with `torch.compile`
- Ahead-of-time with `torch.export`+`AOTInductor`

[ torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) works great in standard environments: it compiles your model the first time it runs, and reuses the optimized version for subsequent calls.

However, on ZeroGPU, given that the process is freshly spun up for (almost) every GPU task, it means that `torch.compile` can’t efficiently re-use compilation and is thus forced to rely on its [filesystem cache](https://docs.pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html#modular-caching-of-torchdynamo-torchinductor-and-triton) to restore compiled models. Depending on the model being compiled, this process takes from a few dozen seconds to a couple of minutes, which is way too much for practical GPU tasks in Spaces.

This is where **ahead-of-time (AoT) compilation** shines.

With AoT, we can export a compiled model once, save it, and later reload it instantly in any process, which is exactly what we need for ZeroGPU. This helps us reduce framework overhead and also eliminates cold-start timings typically incurred in just-in-time compilation.

But how can we do ahead-of-time compilation on ZeroGPU? Let’s dive in.

Let's go back to our ZeroGPU base example and unpack what we need to enable AoT compilation. For the purpose of this demo, we will use the `black-forest-labs/FLUX.1-dev` model:

```
import gradio as gr
import spaces
import torch
from diffusers import DiffusionPipeline
MODEL_ID = 'black-forest-labs/FLUX.1-dev'
pipe = DiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.bfloat16)
pipe.to('cuda')
@spaces.GPU
def generate(prompt):
    return pipe(prompt).images
gr.Interface(generate, "text", "gallery").launch()
```
In the discussion below, we only compile the

`transformer`component of`pipe`since, in these generative models, the transformer (or more generally, the denoiser) is the most computationally heavy component.

Compiling a model ahead-of-time with PyTorch involves multiple steps:

Recall that we’re going to compile the model *ahead* of time. Therefore, we need to derive example inputs for the model. Note that these are the same kinds of inputs we expect to see during the actual runs. To capture those inputs, we will leverage the `spaces.aoti_capture` helper from the `spaces` package:

```
with spaces.aoti_capture(pipe.transformer) as call:
    pipe("arbitrary example prompt")
```
When used as a context manager, `aoti_capture` intercepts the call to any callable (`pipe.transformer` in our case), prevents it from executing, captures the input arguments that would have been passed to it, and stores their values in `call.args` and `call.kwargs`.

Now that we have example args and kwargs for our transformer component, we can export it to a PyTorch [ ExportedProgram](https://docs.pytorch.org/docs/stable/export.html#torch.export.ExportedProgram) by using 

`torch.export.export````
exported_transformer = torch.export.export(
    pipe.transformer,
    args=call.args,
    kwargs=call.kwargs,
)
```
An exported PyTorch program is a computation graph that represents the tensor computations along with the original model parameter values.

Once the model is exported, compiling it is pretty straightforward.

A traditional AoT compilation in PyTorch often requires saving the model on disk so it can be later reloaded. In our case, we’ll leverage a helper function part of the `spaces` package: `spaces.aoti_compile`. It's a tiny wrapper around `torch._inductor.aot_compile` that manages saving and lazy-loading the model as needed. It's meant to be used like this:

```
compiled_transformer = spaces.aoti_compile(exported_transformer)
```
This `compiled_transformer` is now an AoT-compiled binary ready to be used for inference. 

Now we need to bind our compiled transformer to our original pipeline, i.e., the `pipeline`.

A naive and almost working approach is to simply patch our pipeline like `pipe.transformer = compiled_transformer`. Unfortunately, this approach does not work because it deletes important attributes like `dtype`, `config`, etc. Only patching the `forward` method does not work well either because we are then keeping original model parameters in memory, often leading to OOM errors at runtime.

`spaces` package provides a utility for this, too -- `spaces.aoti_apply`:

```
spaces.aoti_apply(compiled_transformer, pipe.transformer)
```
Et voilà! It will take care of patching `pipe.transformer.forward` with our compiled model, as well as [cleaning old model parameters out of memory](https://pypi-browser.org/package/spaces/spaces-0.40.1-py3-none-any.whl/spaces/zero/torch/aoti.py#L87).

To perform the first three steps (intercepting input examples, exporting the model, and compiling it with PyTorch inductor), we need a real GPU. CUDA emulation that you get outside of `@spaces.GPU` function is not enough because compilation is truly hardware-dependent, for instance, relying on micro-benchmark runs to tune the generated code. This is why we need to wrap it all inside a `@spaces.GPU` function and then get our compiled model back to the root of our app. Starting from our original demo code, this gives:

```
  import gradio as gr
  import spaces
  import torch
  from diffusers import DiffusionPipeline
  
  MODEL_ID = 'black-forest-labs/FLUX.1-dev'
  
  pipe = DiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.bfloat16)
  pipe.to('cuda')
  
+ @spaces.GPU(duration=1500) # maximum duration allowed during startup
+ def compile_transformer():
+     with spaces.aoti_capture(pipe.transformer) as call:
+         pipe("arbitrary example prompt")
+ 
+     exported = torch.export.export(
+         pipe.transformer,
+         args=call.args,
+         kwargs=call.kwargs,
+     )
+     return spaces.aoti_compile(exported)
+ 
+ compiled_transformer = compile_transformer()
+ spaces.aoti_apply(compiled_transformer, pipe.transformer)
  
  @spaces.GPU
  def generate(prompt):
      return pipe(prompt).images
  
  gr.Interface(generate, "text", "gallery").launch()
```
With just a dozen lines of additional code, we’ve successfully made our demo quite faster (**1.7x** faster in the case of FLUX.1-dev).

If you want to learn more about AoT compilation, you can read PyTorch's [AOTInductor tutorial](https://docs.pytorch.org/tutorials/recipes/torch_export_aoti_python.html)

Now that we have demonstrated the speedups one can realize under the constraints of operating with ZeroGPUs, we will discuss a few gotchas that came up while working with this setup.

AoT can be combined with quantization to deliver even greater speedups. For image and video generation, the FP8 post-training dynamic quantization schemes deliver good speed-quality trade-offs. However, FP8 requires a CUDA compute capability of at least 9.0 to work. Thankfully, for ZeroGPUs, since they’re based on H200s, we can already take advantage of the FP8 quantization schemes.

To enable FP8 quantization within our AoT compilation workflow, we can leverage the APIs provided by [ torchao](https://github.com/pytorch/ao) like so:

```
+ from torchao.quantization import quantize_, Float8DynamicActivationFloat8WeightConfig
+ # Quantize the transformer just before the export step.
+ quantize_(pipe.transformer, Float8DynamicActivationFloat8WeightConfig())
exported_transformer = torch.export.export(
    pipe.transformer,
    args=call.args,
    kwargs=call.kwargs,
)
```
(You can find more details about TorchAO [here](https://docs.pytorch.org/ao/stable/index.html).)

And we can then proceed with the rest of the steps as outlined above. Using quantization provides another **1.2x** of speedup.

Images and videos can come in different shapes and sizes. Hence, it’s important to also account for shape dynamism when performing AoT compilation. The primitives provided by `torch.export.export` make it easily configurable to provide what inputs should be treated accordingly for dynamic shapes, as shown below.

For the case of Flux.1-Dev transformer, changes in different image resolutions will affect two of its `forward` arguments: 

- `hidden_states`: The noisy input latents, which the transformer is supposed to denoise. It’s a 3D tensor, representing- `batch_size, flattened_latent_dim, embed_dim`. When the batch size is fixed, it’s the- `flattened_latent_dim`that will change for any changes made to image resolutions.
- `img_ids`: A 2D array of encoded pixel coordinates having a shape of- `height * width, 3`. In this case, we want to make- `height * width`dynamic.

We start by defining a range in which we want to let the (latent) image resolutions vary.
To derive these value ranges, we inspected the shapes of [ hidden_states](https://github.com/huggingface/diffusers/blob/0ff1aa910cf3d87193af79ec1ae4487be542e872/src/diffusers/pipelines/flux/pipeline_flux.py#L920) in the pipeline with respect to varied image resolutions. The exact values are model-dependent and require manual inspection and some intuition. For Flux.1-Dev, we ended up with:

```
transformer_hidden_dim = torch.export.Dim('hidden', min=4096, max=8212)
```
We then define a map of argument names and which dimensions in their input values we expect to be dynamic:

```
transformer_dynamic_shapes = {
    "hidden_states": {1: transformer_hidden_dim}, 
    "img_ids": {0: transformer_hidden_dim},
}
```
Then we need to make our dynamic shapes object replicate the structure of our example inputs. The inputs that do not need dynamic shapes must be set to `None`. This can be done very easily with PyTorch [tree_map](https://github.com/pytorch/pytorch/blob/2f0de0ff9361ca4f2b1e6f9edbc600b5fb6abcd6/torch/utils/_pytree.py#L1341-L1373) utility:

```
from torch.utils._pytree import tree_map
dynamic_shapes = tree_map(lambda v: None, call.kwargs)
dynamic_shapes |= transformer_dynamic_shapes
```
Now, when performing the export step, we simply supply `transformer_dynamic_shapes` to `torch.export.export`:

```
exported_transformer = torch.export.export(
    pipe.transformer,
    args=call.args,
    kwargs=call.kwargs,
    dynamic_shapes=dynamic_shapes,
)
```
Check out

[this Space](https://huggingface.co/spaces/zerogpu-aoti/FLUX.1-Kontext-Dev-fp8-dynamic)that shows how to use both quantization and dynamic shapes during the export step.

Dynamic shapes is sometimes not enough when dynamism is too important.

This is, for instance, the case with the Wan family of video generation models if you want your compiled model to generate different resolutions. One thing can be done in this case: compile one model per resolution while keeping the model parameters shared and dispatching the right one at runtime

Here is a minimal example of this approach: [zerogpu-aoti-multi.py](https://gist.github.com/cbensimon/8dc0ffcd7ee024d91333f6df01907916). You can also see a fully working implementation of this paradigm in the [Wan 2.2 Space](https://huggingface.co/spaces/zerogpu-aoti/wan2-2-fp8da-aoti-faster/blob/main/optimization.py).

Since the ZeroGPU hardware and CUDA drivers are perfectly compatible with Flash-Attention 3 (FA3), we can use it in our ZeroGPU Spaces to speed things up even further. FA3 works with ahead-of-time compilation. So, this is ideal for our case.

Compiling and building FA3 from source can take several minutes, and this process is hardware-dependent. As users, we wouldn’t want to lose precious ZeroGPU compute hours. This is where Hugging Face [ kernels library](https://github.com/huggingface/kernels) comes to the rescue. It provides access to pre-built kernels that are compatible for a given hardware. For example, when we try to run:

```
from kernels import get_kernel
vllm_flash_attn3 = get_kernel("kernels-community/vllm-flash-attn3")
```
It tries to load a kernel from the [ kernels-community/vllm-flash-attn3](https://huggingface.co/kernels-community/vllm-flash-attn3) repository, which is compatible with the current setup. Otherwise, it will error out due to incompatibility issues. Luckily for us, this works seamlessly on the ZeroGPU Spaces. This means we can leverage the power of FA3 on ZeroGPU, using the 

`kernels` library.Here is a [fully working example of an FA3 attention processor](https://gist.github.com/sayakpaul/ff715f979793d4d44beb68e5e08ee067#file-fa3_qwen-py) for the Qwen-Image model.

So far, we have been compiling the full model. Depending on the model, full model compilation can lead to significantly long cold start times. Long cold start times make the development experience unpleasant.

We can also choose to compile *regions* within a model, significantly reducing the cold start times, while retaining almost all the benefits of full model compilation. Regional compilation becomes promising when
a model has repeated blocks of computation. A standard language model, for example, has a number of
identically structured Transformer blocks.

In our example, we can compile the repeated blocks of the Flux transformer ahead of time, and propagate the compiled graph to the remaining repeated blocks. The [Flux Transformer](https://github.com/huggingface/diffusers/blob/c2e5ece08bf22d249c62e964f91bc326cf9e3759/src/diffusers/models/transformers/transformer_flux.py) has two kinds of repeated blocks: `FluxTransformerBlock` and `FluxSingleTransformerBlock`.

You can check out [this Space](https://huggingface.co/spaces/cbensimon/FLUX.1-dev-fa3-aoti/tree/main) for a complete example.

💡 For Flux.1-Dev, switching to regional compilation reduces the compilation time from

6 minutesto just30 secondswhile delivering identical speedups.

Once a model (or even a model block) is compiled ahead of time, we can serialize the compiled graph module as an artifact and reuse later. In the context of a ZeroGPU-powered demo on Spaces, this will significantly cut down the demo startup time by skipping the compilation time.

To keep the storage light, we can just save the compiled model graph without including any model parameters inside the artifact.

Check out [this collection](https://huggingface.co/collections/zerogpu-aoti/using-compiled-graph-from-the-hub-68c2afcc03de7609f9f91e35) that shows a full workflow of obtaining compiled model graph, pushing it
to the Hub, and then using it to build a demo. 

- [FLUX.1-dev without AoTI](https://huggingface.co/spaces/zerogpu-aoti/FLUX.1-dev-base)
- [FLUX.1-dev with AoTI and FA3](https://huggingface.co/spaces/zerogpu-aoti/FLUX.1-dev-fa3-aoti)(- **1.75x**speedup)

- [Regional compilation recipe](https://docs.pytorch.org/tutorials/recipes/regional_compilation.html)
- [Regional compilation with AOT](https://docs.pytorch.org/tutorials/recipes/regional_aot.html)
- [Native integration in Diffusers](https://huggingface.co/docs/diffusers/main/en/optimization/fp16)
- [More performance numbers](https://pytorch.org/blog/torch-compile-and-diffusers-a-hands-on-guide-to-peak-performance/)

ZeroGPU within Hugging Face Spaces is a powerful feature that enables AI builders by providing access to powerful compute. In this post, we showed how users can benefit from PyTorch’s ahead-of-time compilation techniques to speed up their applications that leverage ZeroGPU.

We demonstrate speedups with Flux.1-Dev, but these techniques are not limited to just this model. Therefore, we encourage you to give these techniques a try and provide us with feedback in this [community discussion](https://huggingface.co/spaces/zerogpu-aoti/README/discussions/1).

- Visit our [ZeroGPU-AOTI org on the Hub](https://huggingface.co/zerogpu-aoti)to refer to a collection of demos that leverage the techniques discussed in this post.
- Browse `spaces.aoti_*`APIs[source code](https://pypi-browser.org/package/spaces/spaces-0.40.1-py3-none-any.whl/spaces/zero/torch/aoti.py)to learn more about the interface
- Check out [Kernels Community org on the hub](https://huggingface.co/kernels-community)
- Learn more about regional compilation from [here](https://huggingface.co/blog/pytorch.org/tutorials/recipes/regional_compilation.html)
- Upgrade to [Pro](https://huggingface.co/pro)on Hugging Face to create your own ZeroGPU Spaces (and get 25 minutes of H200 usage every day)

*Acknowledgements: Thanks to ChunTe Lee for creating an awesome thumbnail for this post. Thanks to Pedro and Vaibhav for providing feedback on the post. Thanks to Angela Yi from the PyTorch team for helping us with AOT guidance.*

  Updated   •  42k  •  43 

✒

 489

Fast 8 step inference of Qwen Image Edit

⚡

 24

Kontext image editing on FLUX[dev]

⚡

 5

Kontext image editing on FLUX[dev]

💻

Generate images from text prompts

💻

 1

Generate images from text prompts

🎥

 3.32k

generate a video from an image with a text prompt

More Articles from our Blog

transformerspytorchoptimization

 
- +3

 188

 September 11, 2025 transformerspytorchoptimization

  63

 May 14, 2026
