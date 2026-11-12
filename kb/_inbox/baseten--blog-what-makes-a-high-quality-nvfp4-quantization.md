---
title: What makes a high-quality NVFP4 quantization?
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/what-makes-a-high-quality-nvfp4-quantization
author: Chloe Florit
published: '2026-10-09'
fetched: '2026-11-12T06:08:48Z'
classifier: null
taxonomy_rev: 2
words: 1506
content_sha256: f14009770d6a40e2b7489dace28489ca6d2b3a4fcc0bef5f4da6f8b0bcffe803
---

# What makes a high-quality NVFP4 quantization?

Model performance
# What makes a high-quality NVFP4 quantization?

NVFP4 makes models smaller and faster, but quantizing some layers can hurt quality. An intuitive look at how to choose which layers can run at 4 bits.


- Authors
- Date
- October 9, 2026

TLDR

A high-quality NVFP4 quantization comes down to choosing which layers can run at 4 bits and which need more precision. This post covers three ways to assign a format to each layer: heuristic-based algorithms decide by architecture; isolated-layer sensitivity scoring measures one layer at a time, so its scores can't be added; and SaturationQuant builds saturation into each score, so they can be added across a mixed-precision recipe. Saturation means each layer adds less loss when others are quantized.

Quantization makes a model smaller and faster by storing its weights and activations in a lower-precision format. NVFP4 represents each value in 4 bits.

With such coarse rounding, some layers lose information the model relies on. Other layers handle 4 bits with almost no decrease in output quality. The key is to determine which layers can run at 4 bits and which need more precision.

In this post, I'll explain how we optimize for high-quality 4-bit quantization by walking through three approaches: heuristic rules, isolated-layer sensitivity scoring, and SaturationQuant.

Model weights are stored in VRAM (high-bandwidth memory attached to the GPU). During inference, the GPU has to move those weights from VRAM into its compute units (e.g., registers or shared memory) to perform calculations.

If you cut the weight size, you cut the bytes you must fetch by \~2x or \~4x. For example, FP16 uses 2 bytes per weight, while FP8 uses 1 byte, and FP4 uses 0.5 bytes.

In a compute-bound workload, the GPU spends most of its time doing arithmetic rather than moving weights and activations from VRAM into its compute units. For an LLM, most of that arithmetic is matrix multiplication, which runs on the GPU's tensor cores. The benefit of quantization for compute-bound workloads is higher arithmetic throughput: on hardware like NVIDIA Blackwell GPUs with native FP4 support, FP4 tensor core operations can deliver up to 4× the peak FLOPS of FP16.

**Weights** are parameters learned during training. They stay fixed at inference. Each connection between two neurons has a weight, and each layer has its own tensor of weights.

**Activations:** During inference, activations are created from the input and weights. Each neuron combines the values reaching it, then passes the result through a nonlinearity. That output is its activation.

Depending on the quantization configuration, a layer’s weights, activations, or both can be quantized to a lower-precision format. Each value has to be rounded to one of the few numbers that 4 bits can represent.

FP4 can only represent a fixed set of 15 values: 0, ±0.5, ±1, ±1.5, ±2, ±3, ±4, ±6, but weights and activations are often much smaller than that. Each group of weights or activations has its own dynamic range, the span from its smallest to largest value. A scale maps the grid onto the range the values fall in (fit to the largest absolute value). Weights and activations use separate scales since their ranges are unrelated.

*For clarity, the following diagrams omit NVFP4’s tensor-level FP32 scale and show only the block-level scaling step.*

With NVFP4, a tensor (e.g., an array of weights or activations) is split into blocks of 16 consecutive values, and each block sets its own scale.

If we have one scale for the entire array of weights, for example, then the largest outlier will impact all the other values during quantization. The scale is set by that outlier. Let's say the array's biggest value is 84 while the rest sit around 1 or 2. The scale becomes 84 ÷ 6 = 14, so the magnitudes NVFP4 can represent now read 0, 7, 14, 21, 28, 42, 56, 84, and every value below 3.5 is closer to 0 than to 7.

Weight scales can be calculated from the weights since they're fixed. But activations only exist once an input runs through the model, so their ranges have to be measured first through calibration.

Calibration runs a small set of representative inputs through the model and records the distribution of activation values. These statistics are used to calculate the scales.

Calibration involves three steps:

1. **Choose a calibration dataset:** Select examples that accurately reflect the structure, content, and workload types (e.g., coding or agentic tasks) of your expected inputs and outputs. Run the examples through the model to record the distribution of activation values.
2. **Choose a clipping range**: Quantization must map activations into a limited set of representable values. Using the minimum and maximum avoids clipping, but rare outliers can widen the range and reduce precision for the majority of activations. Percentile-, histogram-, and error-based calibration methods may clip a small number of outliers to represent the model’s typical activation values more precisely.
3. **Compute the activation scales:** Divide each activation tensor into blocks of 16 values. For every block, find its largest absolute value and use it to compute a scale that maps the block’s values into NVFP4’s representable range of −6 to 6.

Heuristic-based algorithms determine each layer's precision based on the architecture instead of measuring how sensitive each layer is to quantization. (Measuring sensitivity requires a calibration dataset, quantizing layer by layer, and comparing outputs against the full-precision model.) A common heuristic is to quantize MoE expert matrices to a lower precision while keeping attention layers at higher precision, since attention is often more sensitive to quantization. This saves memory because expert weight matrices account for most of an MoE model’s parameters. In short, in many MoE LLMs, expert layers are more robust to quantization than attention layers.

[NVIDIA ModelOpt](https://github.com/NVIDIA/Model-Optimizer) provides predefined configurations that implement architecture-based quantization heuristics:

- `NVFP4_EXPERTS_ONLY_CFG` quantizes only MoE expert layers.
- `NVFP4_MLP_ONLY_CFG` quantizes MLP and MoE layers while leaving attention layers at higher precision.

Unlike ModelOpt AutoQuantize (see below), these configurations do not measure each layer’s sensitivity to decide its precision. Each layer's precision is based on architecture.

*Note: MoE is an architecture where the model is divided into many specialized sub-networks (experts), but only a small subset activates for any given token.* 

[AutoQuantize](https://nvidia.github.io/Model-Optimizer/reference/generated/modelopt.torch.quantization.model_quant.html#modelopt.torch.quantization.model_quant.auto_quantize) chooses a precision format for each layer (e.g., NVFP4, FP8, leaving it unquantized). Using the sensitivity scores, AutoQuantize picks the combination of formats that minimizes the estimated loss without exceeding a target memory size.

AutoQuantize supports three sensitivity scoring methods: gradient-based, KL divergence, and Aumann–Shapley.

Sensitivity is how much rounding a layer’s weights and activations to a lower-precision format affects the model’s output. Some layers can use lower-precision formats like NVFP4 with almost no change in model output quality. Other layers lose information the model relies on, so AutoQuantize assigns them higher-precision formats.

The gradient method estimates how much the model's loss would increase if one layer were quantized to a given format while every other layer stayed at its baseline configuration.

AutoQuantize has four stages:

A candidate format is one of the quantization formats AutoQuantize tries for each layer, such as FP8 or NVFP4. You choose the candidates with `quantization_formats`, and "no quantization" is always included as an option. The cost limit is the target memory size (or number of bits).

python

```
model, search_state = mtq.auto_quantize(
    model,
    constraints={"effective_bits": 4.8},
    quantization_formats=["NVFP4_DEFAULT_CFG", "FP8_DEFAULT_CFG"],
    data_loader=calib_loader,
    forward_step=forward_step,
    loss_func=loss_func,
    method="gradient"
)
```
AutoQuantize uses sensitivity scores to compare mixed-precision recipes and decide which quantization format to assign to each layer. To estimate the increase in loss from quantizing several layers at once, AutoQuantize can’t just add up their individual sensitivity scores.

The effect of quantizing a layer depends on how much of the model has already been quantized. Quantizing a layer often adds less loss when other layers are already quantized. Adding the isolated scores can overestimate the loss of the complete recipe.

Loss is effectively bounded. Each new quantized layer consumes a fraction of the remaining loss headroom\*. As more layers are quantized, the total increase in loss begins to saturate.

*\*headroom: the gap between the current loss and the maximum it can reach.*

[SaturationQuant](https://arxiv.org/pdf/2607.12266) scores each layer by taking into account the other quantized layers, using Aumann–Shapley scoring. Saturation is built into the score, so the scores can be added. The sum of these scores more accurately predicts the loss that recipe produces.

```
model, search_state = mtq.auto_quantize(
    model,
    quantization_formats=["NVFP4_DEFAULT_CFG", "FP8_DEFAULT_CFG"],
    data_loader=calib_loader,
    forward_step=forward_step,
    method="aumann_shapley"
)
```
Some layers can run in NVFP4 with almost no change in quality, while others need FP8 or higher precision. Calibration data is used to measure activation ranges, and scales map weights and activations onto the NVFP4 grid. To choose which layers to run in NVFP4:

- Use architecture-based heuristics when you need a fast recipe without running a layer-by-layer search.
- Use gradient scoring when you can calculate loss on a representative calibration dataset and want to measure each layer’s sensitivity.
- Use Aumann–Shapley scoring when you have a tighter memory target and need to estimate how the complete mixed-precision recipe will affect quality.
