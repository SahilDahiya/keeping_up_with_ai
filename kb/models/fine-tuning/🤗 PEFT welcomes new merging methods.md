---
title: 🤗 PEFT welcomes new merging methods
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Adds LoRA adapter merging to PEFT via add_weighted_adapter, supporting linear/cat/TIES/DARE
  (and their SVD variants) so multiple adapters from the same base model can be combined
  on the fly without downloading and merging full checkpoints. Explains when TIES/DARE's
  sign-election and drop-and-rescale steps beat naive weighted averaging.
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/peft_merging
author: Sourab Mangrulkar; Sayak Paul
published: '2024-02-19'
fetched: '2026-07-14T22:06:50Z'
classifier: claude
taxonomy_rev: 1
words: 2441
content_sha256: 089b09f0403bbe7135e5077283fbcd4574c2eb62f2f18407b9b9bcceba64e7ff
---

# 🤗 PEFT welcomes new merging methods

Text-to-Image •  Updated   •  159  •  15  

#### CiroN2022/toy-face

![](https://cdn-avatars.huggingface.co/v1/production/uploads/63061acddf993a789e640121/BA1YishqUl_XR5Rs_DaC4.jpeg) 

 Published
					February 19, 2024 

  Upvote 

 31

The typical way of model merging, so far, has been to take a set of models and merge them. [This post](https://huggingface.co/blog/mlabonne/merge-models) gives a nice primer on this topic. Generally, for merging multiple models, we first download their checkpoints and then perform merging. Depending on the merge algorithm and the sizes of the underlying model, this process can be quite memory-intensive. The `mergekit` library provides optimized ways for handling this, making the process manageable on limited memory. 

But what if we wanted to merge different “adapters” obtained from the * same* model? You might have four different LoRA checkpoints obtained from the same base model, and you want to experiment with different merging techniques. Eventually, you want to settle with the best merge, giving you the best results for your task. A couple of things become evident when approaching such a developer experience:

- When dealing with adapters such as LoRA, it’s common for users to swap in and out different adapters or even combine them. Adapters can be activated, de-activated, or completely swapped out of the memory. Therefore, we need to do the “merging” part on the fly (as opposed to the method described above) to provide a seamless experience to the users.
- Different adapters might have different requirements for merging. The merging algorithm for LoRA might not equally translate to IA3, for example.

With these aspects in mind, we [shipped](https://github.com/huggingface/peft/pull/1364) new merging methods targeting the popular LoRA adapters in 🤗 PEFT. In this post, we want to take you through the methods available, code examples to help you get cracking, impressive results, and our future plans. Let’s get started 🚀

- [Methods for combining/merging LoRA adapters](https://huggingface.co#methods-for-combiningmerging-lora-adapters)
- [How do I merge my LoRA adapters?](https://huggingface.co#how-do-i-merge-my-lora-adapters)
- [Extending to text-to-image generation](https://huggingface.co#extending-to-text-to-image-generation)
- [Observations](https://huggingface.co#observations)

`cat`)
	
In this method, the LoRA matrices are concatenated. For example, if we have 2 LoRA adapters and along with weights and for weighted merging of these two adapters, then the merging happens as follows:



where .

Now, the output of this new merged LoRA layer would be as if the original 2 LoRAs were active with weights and for applied to the first and second adapters, respectively.


Here, we can observe that:


🧠 This is the exact weighted merging of LoRA adapters. It is also available via [PEFT integration of Diffusers](https://huggingface.co/docs/diffusers/main/en/tutorials/using_peft_for_inference) when you call 

`set_adapters()`  wherein instead of creating a new merged adapter, the active adapters are combined sequentially, as shown on the right-hand side of the above equation. When using this method, it allows for participating LoRA adapters to have different ranks.
`linear`)
	
In this method, the LoRA matrices are involved in weighted sum. This is what the Task arithmetic paper implements on task weights. In task arithmetic, one first computes the task weights which is difference between finetuned weights and base model weights, then does a weighted sum of these task weights. Here, the delta weights considered are the individual matrices and instead of their product . This method can be applied only when all the participating LoRA adapters have same rank.

Let’s go through an example. Consider 2 LoRA adapters & along with weights and for weighted merging of these two adapters, then the merging happens as follows:



For more details, please refer to the paper: [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089).

`svd`)
	
Instead of considering individual matrices and as task weights, their product which is the delta weight is considered the task weight.

Let’s continue with the example from the previous sub-sections. Here, first the delta weight of merged combination is computed as follows:


After getting the above-merged delta weight, SVD (singular value decomposition) is applied to get the approximates and :

🧠 Similar to 

`cat` method, this method also allows for LoRA adapters with different ranks. In addition, one can choose the rank for the resultant merged LoRA adapter which defaults to the maximum rank among the participating LoRA adapters. A limitation of this approach is that it requires a lot of GPU memory for performing the SVD operation.
`ties` , `ties_svd` )
	
This builds upon the `linear` and `svd` methods by changing the way merged adapters are computed from task weights and result in the `ties` and `ties_svd` methods, respectively. In TIES (TRIM, ELECT SIGN & MERGE), one first computes the task weights which in our case would be the LoRA adapters ,  for non svd variant and their product  for svd variant. After this, you prune the smallest values of the task weights and retain the top-k values based on the specified fraction `density` . Then, you calculate the majority sign mask from the participating pruned task weights, multiply task tensors with the user provided weightage followed by disjoint merge based on the majority sign mask. For majority sign mask computation, you have two options:

- `total`considers the magnitude as well as sign to get the majority sign, i.e., sum up all the corresponding weights;
- `frequency`only considers the weight sign to obtain the majority sign, i.e., sum up the sign of all the corresponding weights.

For more details, refer to the paper: [TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708).

`dare_linear` , `dare_ties` , `dare_linear_svd` , `dare_ties_svd` )
	
This also builds upon the `linear` and `svd` methods wherein the task weights are LoRA adapters ,  for non svd variant and their product  for svd variant. `DARE` method proposed in [Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099) first randomly prunes the values of the task weight based on the specified fraction `1-density`, and then rescales the pruned task weights by `1/density`. `DARE` is a general plug-in and can be applied to any existing model merging methods. We have implemented `DARE` with Linear/Task Arithmetic (`*_linear*`) and TIES (`*_ties*`).

For `*_linear*` variants of `DARE`, we first use `DARE` to randomly prune task weights and then perform weighted sum of task tensors based on user specified weightage for participating LoRA adapters.

For `*_ties*`  variants of `DARE`, we first use `DARE` to get the pruned task weights, then adopt the last 2 steps of `ties`, i.e., calculating majority sign mask and using the mask to perform disjoint merge of the task weights.

`magnitude_prune` , `magnitude_prune_svd` )
	
This also builds upon the `linear` and `svd` methods wherein the task weights are LoRA adapters ,  for non svd variant and their product  for svd variant. In this method, you first prune the smallest values of the task weights and retain the top-k values based on the specified fraction `density`.  Then, you carry out the weighted sum of task tensors based on user-specified weightage for participating LoRA adapters.

In PEFT, when using LoRA, you can use the class method [ add_weighted_adapter()](https://huggingface.co/docs/peft/main/en/package_reference/lora#peft.LoraModel.add_weighted_adapter) to try the different combining methods. For example, below you can see how we can combine three LoRA adapters using 

`ties` method and the resulting generations from the new merged adapter. ![instruct_ad_sql](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/instruct_ad_sql.png)


You can find the above example in the PEFT repo’s [examples](https://github.com/huggingface/peft/blob/main/examples/multi_adapter_examples/Lora_Merging.ipynb). 

Let’s take another example, as shown below, using `magnitude_prune` method and the resulting generations. 

![mental_health_hinglish](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/mental_health_hinglish.png)


Now, what if we want to use the merged adapters capability to answer a mental health related query in Hinglish? This would require capabilities from both the adapters to be used. Below we can see the results on the query “Sad feelings ko kaise dur kare?” (Translation: How to get rid of sad feelings?). When, all adapters are disabled and the base model is used, the response starts with it being an AI followed by general suggestions. When hinglish adapter is enabled, the response is in Hinglish and short following the finetuning data but doesn’t do a good job at giving concrete suggestions to help overcome sadness. When mental_health adapter is enabled, the response is akin to what a human would say but sadly it isn’t in Hinglish. When merge adapter is enabled, we can see that the response is in Hinglish and short while giving concrete suggestions which can be found in the response of mental_health adapter such as exercising, spending time with friends, reading, meditation and focusing on positive thinking. Therefore, we can observe that merging adapters can lead to combining their individual capabilities to support new use cases.

![instruct_ad_sql](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/merged_capabilities.png)


Finally, let’s take the example of `dare_linear`  and check the resulting generations.

![ad_sql](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/ad_sql.png)


We have a dedicated developer guide for these merging methods in PEFT which you can find [here](https://huggingface.co/docs/peft/developer_guides/model_merging). 

In this section, we show you how to take advantage of these merging methods for text-to-image generation using 🤗 Diffusers. Note that Diffusers [already relies on PEFT](https://huggingface.co/docs/diffusers/main/en/tutorials/using_peft_for_inference) for all things LoRA, including training and inference. However, currently, it’s not possible to benefit from the new merging methods when calling [ set_adapters()](https://huggingface.co/docs/diffusers/main/en/api/loaders/unet#diffusers.loaders.UNet2DConditionLoadersMixin.set_adapters) on a Diffusers pipeline.  This is why we are 

But thanks to PEFT, there’s always a way to circumvent around this. We will use the [ add_weighted_adapter()](https://huggingface.co/docs/peft/main/en/package_reference/lora#peft.LoraModel.add_weighted_adapter) functionality for this. Precisely, these are the steps that we will take to combine the 

- Obtain `PeftModel`s from these LoRA checkpoints.
- Merge the `PeftModel`s using the`add_weighted_adapter()`method with a merging method of our choice.
- Assign the merged model to the respective component of the underlying `DiffusionPipeline`.

Let’s see this in action. All the code shown in the parts below come from [this Colab Notebook](https://colab.research.google.com/github/huggingface/peft/blob/main/examples/multi_adapter_examples/multi_adapter_weighted_inference_diffusers.ipynb). 

Since both the LoRA checkpoints use [SDXL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) UNet as the their base model, we will first load the UNet:

```
from diffusers import UNet2DConditionModel
import torch
unet = UNet2DConditionModel.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16, 
    use_safetensors=True,
    variant="fp16",
    subfolder="unet",
).to("cuda")
```
We then load the actual SDXL pipeline and the LoRA checkpoints. We start with the “CiroN2022/toy-face” LoRA:

```
from diffusers import DiffusionPipeline
import copy
sdxl_unet = copy.deepcopy(unet)
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
     variant="fp16",
     torch_dtype=torch.float16,
     unet=unet
).to("cuda")
pipe.load_lora_weights("CiroN2022/toy-face", weight_name="toy_face_sdxl.safetensors", adapter_name="toy")
```
Now, obtain the `PeftModel` from the loaded LoRA checkpoint:

```
from peft import get_peft_model, LoraConfig
toy_peft_model = get_peft_model(
    sdxl_unet,
    pipe.unet.peft_config["toy"],
    adapter_name="toy"
)
original_state_dict = {f"base_model.model.{k}": v for k, v in pipe.unet.state_dict().items()}
toy_peft_model.load_state_dict(original_state_dict, strict=True)
```
💡 You can optionally push the `toy_peft_model` to the Hub using: `toy_peft_model.push_to_hub("toy_peft_model", token=TOKEN)`.

Next, we do the same for the “nerijs/pixel-art-xl” LoRA:

```
pipe.delete_adapters("toy")
sdxl_unet.delete_adapters("toy")
pipe.load_lora_weights("nerijs/pixel-art-xl", weight_name="pixel-art-xl.safetensors", adapter_name="pixel")
pipe.set_adapters(adapter_names="pixel")
pixel_peft_model = get_peft_model(
    sdxl_unet,
    pipe.unet.peft_config["pixel"],
    adapter_name="pixel"
)
original_state_dict = {f"base_model.model.{k}": v for k, v in pipe.unet.state_dict().items()}
pixel_peft_model.load_state_dict(original_state_dict, strict=True)
```
Now, we are all equipped with weighted adapter inference! We start by loading all the necessary things:

```
from peft import PeftModel
from diffusers import UNet2DConditionModel, DiffusionPipeline
import torch
base_unet = UNet2DConditionModel.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16, 
    use_safetensors=True,
    variant="fp16",
    subfolder="unet",
).to("cuda")
toy_id = "sayakpaul/toy_peft_model"
model = PeftModel.from_pretrained(base_unet, toy_id, use_safetensors=True, subfolder="toy", adapter_name="toy")
model.load_adapter("sayakpaul/pixel_peft_model", use_safetensors=True, subfolder="pixel", adapter_name="pixel")
```
Now, combine the LoRA adapters — the moment we all have been waiting for!

```
model.add_weighted_adapter(
    adapters=["toy", "pixel"],
    weights=[0.7, 0.3],
    combination_type="linear",
    adapter_name="toy-pixel"
)
model.set_adapters("toy-pixel")
```
Here, we are just starting with the “linear” merging strategy but will experiment with other exotic merging algorithms, such as TIES. We finally assign the `model` to our `DiffusionPipeline` and perform inference:

```
model = model.to(dtype=torch.float16, device="cuda")
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", unet=model, variant="fp16", torch_dtype=torch.float16,
).to("cuda")
prompt = "toy_face of a hacker with a hoodie, pixel art"
image = pipe(prompt, num_inference_steps=30, generator=torch.manual_seed(0)).images[0]
image
```
![toy_face_hacker](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/toy_face_hacker.png)


Let’s try `ties_svd` method. You can find the example notebook [here](https://github.com/pacman100/peft-dreambooth-ui/blob/main/lora_merging.ipynb).

```
pipe.unet.add_weighted_adapter(
    ["teapot","watercolour"], 
    [1.0, 1.0],
    "merge",
    combination_type="ties_svd",
    density=0.5
)
```
![cat_teapot](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/cat_teapot.png)


Now, let’s try combining two style LoRAs using `dare_linear`:

```
model.add_weighted_adapter(
    adapters=["toy", "pixel"],
    weights=[1.0, 1.0],
    combination_type="dare_linear",
    adapter_name="merge",
    density=0.7
)
```
![toy_face_pixel_art.png](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/toy_face_pixel_art.png)


Now, let’s try `ties`  method with `majority_sign_method="frequency"` :

```
model.add_weighted_adapter(
    adapters=["toy", "sticker"],
    weights=[1.0, 1.0],
    combination_type="ties",
    adapter_name="merge",
    density=0.5,
    majority_sign_method="frequency"
)
```
![indian_goddess](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/peft_merging/indian_goddess.png)


- In most scenarios, `cat`method will give great results. So, start with that. However, note that if you combine many adapters, the resulting merged adapter can have a large size due to concatenation leading to OOM. So, when exploring few adapters,`cat`would be a good starting point.
- In you want to explore or `cat`isn’t working, try`linear`,`maginuted_prune`and`dare_linear`in that order. For`maginuted_prune`and`dare_linear`, we found that higher`density`values around 0.7-0.8 work better.
- When using `ties`, we found that in many cases`majority_sign_method="frequency"`to perform better than`majority_sign_method="total"`(`total`is currently the default). For ties, a good default value for`density`is 0.5. You can then try tuning this lower or higher based on your observations post merging the adapters.
- `dare_ties`wasn’t giving good results.
- When working with Stable Diffusion LoRA adapters that have different ranks, you can try the `*svd`family of methods. Note that these require more GPU memory and take around ~1.5 minutes to create the merged adapter due to the expensive SVD operations.`ties_svd`gave good result when combining`subject`+`style`LoRAs as seen in an example above. When combining 2`style`adapters,`dare_linear`with high`density`or`ties`with`majority_sign_method="frequency"`seems to work better as seen in the examples above.

We’re grateful to Le Yu and Prateek Yadav, authors of DARE and TIES, for their generous feedback and guidance on the [PR](https://github.com/huggingface/peft/pull/1364). To honor their efforts, we have added them as the co-authors of the PR. Thanks to Prateek and Le for reviewing the blog post draft as well.

- [Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089)
- [TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)
- [Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099)
- [mergekit](https://github.com/cg123/mergekit): Tools for merging pretrained large language models.
- [PEFT integration in Diffusers](https://huggingface.co/docs/diffusers/main/en/tutorials/using_peft_for_inference)
- [Model merging guide for PEFT users](https://huggingface.co/docs/peft/developer_guides/model_merging)

```
@inproceedings{
    ilharco2023editing,
    title={Editing models with task arithmetic},
    author={Gabriel Ilharco and Marco Tulio Ribeiro and Mitchell Wortsman and Ludwig Schmidt and Hannaneh Hajishirzi and Ali Farhadi},
    booktitle={The Eleventh International Conference on Learning Representations },
    year={2023},
    url={https://openreview.net/forum?id=6t0Kwf8-jrj}
}
```
```
@inproceedings{
    yadav2023tiesmerging,
    title={{TIES}-Merging: Resolving Interference When Merging Models},
    author={Prateek Yadav and Derek Tam and Leshem Choshen and Colin Raffel and Mohit Bansal},
    booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
    year={2023},
    url={https://openreview.net/forum?id=xtaX3WyCj1}
}
```
```
@misc{yu2023language,
    title={Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch}, 
    author={Le Yu and Bowen Yu and Haiyang Yu and Fei Huang and Yongbin Li},
    year={2023},
    eprint={2311.03099},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
```
@misc{
    mergekit,
    author = {Charles O. Goddard and contributors},
    title = {mergekit},
    year = {2023},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\url{https://github.com/arcee-ai/mergekit}}
}
```
 Text-to-Image •  Updated   •  159  •  15 

 Text-to-Image •  Updated   •  14.2k  •  628 

 Text-to-Image •  Updated   •  1.41M  •  7.93k 

More Articles from our Blog

peftloraguide

  75

 June 18, 2026 llmintelnlp

 
- +1

 25

 September 29, 2025 I got very confused by the claim that **linear** corresponds to the **task arithmetic** paper.

This paper operates on the **weight difference** between base and FT models, so the difference when applying LoRA is a vector of dimension `(num_params,)` with:

- **0s**on modules not LoRAed
- **BA.flatten()**on modules that got a LoRA

The merging from this paper then corresponds to **CAT** and **not linear** in my opinion. The flattened LoRA weights don't make any sense in this context imo.
