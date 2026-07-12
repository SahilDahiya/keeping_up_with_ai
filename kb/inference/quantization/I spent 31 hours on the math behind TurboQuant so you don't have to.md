---
title: I spent 31 hours on the math behind TurboQuant so you don't have to
topic: inference
subtopic: quantization
secondary_topics:
- models/reasoning
summary: Mathematical deep dive into TurboQuant and its quantization behavior for
  LLM inference.
source: baseten
url: https://www.baseten.co/blog/i-spent-31-hours-on-the-math-behind-turboquant-so-you-dont-have-to/
author: Ali Taha
published: '2026-03-27'
fetched: '2026-07-11T04:05:51Z'
classifier: codex
taxonomy_rev: 1
words: 3020
content_sha256: 2e9e0c984a83f2e1a945ed496f16057efd1f7881e102802e6ad3ef397ae1cdb0
triage: keep
skip_reason: null
---

# I spent 31 hours on the math behind TurboQuant so you don't have to

![Turboquant](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774567692-photo-frame-1.png%3Fauto%3Dformat%26fit%3Dcrop%26h%3D630%26w%3D1200&w=3840&q=100)

How does [TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) actually work? Is it worth the hype? Is it any different from modern quantization techniques like Nvidia's FP4?

![polar](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774563699-hevwgs9byaawlfn.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Conditioning of PolarQuantTo understand TurboQuant, one must first understand PolarQuant:

a novel quantization method employing random preconditioning and polar transformation. Our method transforms the KV embeddings into polar coordinates using a recursive algorithm and then quantizes resulting angles. The long-context evaluation demonstrates that PolarQuant compresses the KV cache by over 4.2x

That's a lot to take in. Let's break it down. From the very beginning:

## KV Cache: The problem

![Attention is all you need](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774569729-attention.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Every transformer-based LLM computes attention the same way. For each token, the model produces three vectors: a query (what am I looking for?), a key (what do I contain?), and a value (what information do I carry). Attention scores are computed as softmax(Q·K^T/√d)·V : the query dot-products every key to figure out which tokens matter, then takes a weighted sum of the values.

![Attention KV cache](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774569997-frame-2085654071.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

The trick that makes autoregressive generation fast is KV caching. Once a token's key and value vectors are computed, they never change for a given sequence. So you store them and reuse them for every future token in that request. The problem: this cache grows linearly with sequence length. Every new token adds one key vector and one value vector per layer per head. For Llama-3.1-8B with 32 layers, 8 KV heads, head dimension 128, and 128K context: that's 128,000 × 32 × 8 × 128 × 2 (K and V) × 2 bytes (FP16) = 16 GB of KV cache alone. For a single user session. Add a bunch more concurrent sessions on the same GPU and the KV cache becomes the memory bottleneck.

![kv cache and memory requirement](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774563873-hevo2zwbgaelg_6.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

## Quantization: Existing solutions

Currently, the most aggressive quantization solution is NVFP4 two layer quantization. This was covered in previous posts, but, to give a brief overview, here's how it works:

![NVFP4 two layer quantization](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774570042-frame-2085654074.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

You scan through the entire matrix. You find the global maximum value in the matrix. You then find the maximum value for each block of 16 elements. This gives you a local and global granularity. You divide the number down by the local maximum, and you divide the scales by the global maximum. You then cast the numbers into the closest 4-bit bucket. You do this for both matrices (weights and activations). You multiply the two, making use of specialized cores, which internally will take your scaling factors, reconstruct them, and multiply the result of your matrix multiplication with the inverse of the scaling factors to yank them back into full-precision.

## The bucketing problem

Every quantization method is, at its core, a mapping. You take a continuous number and assign it to the nearest bucket. With 4 bits you have 16 buckets. With 2 bits you have 4. The problem isn't the mapping itself: it's that you need to know where to place the buckets, and that requires measuring your data first.

For each block of values, you compute a scale factor (max value) and a zero-point (offset), store them in full 16-bit precision alongside your quantized values, and use them to reconstruct later. These normalization constants are pure overhead. One outlier corrupts the entire block's precision.

![The Bucketing Problem](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774570088-frame-2085654072.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

How can we fix bucket problem?

What if we knew the distribution of our data ahead of time? What if we could guarantee that all values cluster in a predictable, tight range?

But...there exists *no way* through which we can somehow magically manipulate our data into a tightly clustered distribution to ensure that we can map it effectively. so we pay the price of 2-layered quantization. we accept this mediocrity at face value.

## PolarQuant

The authors at Google Research argue that they *could*, in fact, manipulate the data into a tightly clustered distribution. But how?They state 2 properties of multivariate normal random variables:

- Multiply any fixed vector by a random matrix with bell curve entries. The output is a multivariate Gaussian centered at zero, with variance equal to the squared length of the original vector.

- If every coordinate of a vector is drawn from a standard bell curve, the length of that vector follows a generalized gamma distribution. In high dimensions, this length concentrates tightly around √d.

We will do something more elegant than a proof. We will code.

```
def fact1_gaussian_norms():
    torch.manual_seed(0)
    dims = [16, 64, 128, 512]
    n_samples = 10000
    fig, axes = plt.subplots(1, len(dims), figsize=(5 * len(dims), 5))
    for ax, d in zip(axes, dims):
        x = torch.randn(n_samples, d)
        norms = torch.norm(x, dim=1).numpy()
```
![fact1](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774570133-frame-2085654070.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Distribution proof of fact 1

```
1    tokenizer = AutoTokenizer.from_pretrained("gpt2")
2    model = GPT2LMHeadModel.from_pretrained("gpt2")
3    model.eval()
4    text = "Baseten has the best performance engineers"
5    input_ids = tokenizer.encode(text, return_tensors="pt")
6
7    with torch.no_grad():
8        outputs = model(input_ids, use_cache=True)
9        K = outputs.past_key_values[5][0][0]
10
11    x = K[0, 5]
12    d = x.shape[0]
13    norm_x = torch.norm(x).item()
14
15    n_trials = 10_000
16    torch.manual_seed(0)
17
18    S_all = torch.randn(n_trials, d, d)  # 10K different random matrices
19    y_all = torch.bmm(S_all, x.unsqueeze(0).unsqueeze(-1).expand(n_trials, d, 1))
20    y_all = y_all.squeeze(-1)
```
Proving the second fact, that for any vector x, if S is a random matrix with i.i.d. normal entries, the vector matrix product has a multivariate normal distribution, is just as simple. We pick one token, in this case head 0, layer 5, token 5. It has 64 dimensions. In this case, this token happens to have a norm of 9.85.

We then draw 10k random matrices. We multiply each of these randomized matrices with the vector x. We then analyze the distributions of each dimension.

![fact2](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774570203-fact2.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

This proves to us that, after random preconditioning, vectors behave like Gaussians. Every feature of the vector, sampled across all the products, follow the distribution of a normal random variable.

Satisfied with the above and having seen it work, we can begin to develop some intuition for it.

So we've established two things. First, multiplying any vector by a random matrix produces Gaussian output. Second, the length of a Gaussian vector concentrates tightly around √d. But what does pre-conditioning actually do?

Well, it just combines the above two facts. It generates a random matrix S, and multiplies it by our vector to generate an output that is, in theory, a multivariate Gaussian centered at 0. This means that every coordinate of our new resultant vector acts as though it had been sampled from a standard bell curve.

By the first fact, the length of our vector (or any vector sampled from a standard bell curve for that matter) follows a generalized gamma distribution, which, in high dimensions, guarantees that this length concentrates tightly around √d.

If we apply this to our stored KV cache, our stored K matrix and V matrix, each coordinate in the KV embedding will behave *as though* it were drawn from the same bell curve. Each a random variable drawn from the normal distribution.

![Rotation clustering vectors](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774564470-hev15fcacaackas.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

## Why does this matter

Now we get into the crux of the algorithm.

At a high level, our approach begins by grouping pairs of coordinates of a d-dimensional vector x and transforming each pair into 2D polar coordinates. This produces d/2 radius and angle pairs. Next, we gather d/2 of radii and apply the polar transform to them. This procedure is recursively repeated log(d) times and the final output consists of a single final radius and a collection of 1,2,4,...,d/2-dimensional angle vectors.

So we convert from cartesian and polar. This is easy...when we have two coordinates...

But how do we convert d_embed coordinates? Simple really. Just pair them into groups of 2 coordinates, and each (x1,x2) pair becomes a (r, Θ) pair. You then have a list of d_embed/2 radii and d_embed/2 Θ's. Store the Θ's away. Take all the radii. They become our new coordinate pairs (r1, r2). Each pair becomes converted into (R, Θ). You then have a list of d_embed/4 radii and d_embed/4 Θ's Store the Θ's away. Take all the radii. They become our new coordinate pairs... I think this is why they made for loops. You get the idea. We keep going till the very last pair, the very last R and Θ.

![Polar quantization bubbling up](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774564543-hewgiu6byaaa4hm.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Now, if I haven't lost you, let's think back to what our x1 and x2 (or any pair) of our values will be. After pre-conditioning, they both have the same variance, the same mean, and are drawn from the same N(0, σ²) for some σ, distribution.

What operation are we doing?

What is x2/x1?

Well, when you divide two numbers sampled from the same distribution, the ratio is statistically going to tend to 1. and arctan(1) = π/4 = 45°.

The lemma derived for this in the paper is:

That's the first level. But they can still vary. Angles can vary from anywhere between 0 to 2π (either coordinate x2 or x1 could have been negative), but we both agree that these angles are *centered* around π/4.

Now we get to level 2. Level 1 gave us radius, angle pairs. We take all the radii, and we bring them to the next level.

Now things get interesting. We do arctan(r₂/r₁). Each radius is √(x₁² + x₂²) of two different pairs from the previous level. This means that the possibility that either radius is negative is 0. We are guaranteed to have values exclusively between 0 and π/2. So we do our math, and for each radii pair, we produce a new radius and angle. At level 1, raw coordinates could be negative, so angles spanned the full [0, 2π). Now, radii are always positive, so the angle we produce is locked into [0, π/2]. The angle literally cannot stray as far as the previous level. Also, the angles produced here are even more tightly centered around π/4 than the previous level. Why so?

As we keep recursing, each radius becomes the norm of a longer sub-vector. At level 2, each radius summarizes 2 coordinates (r₁ = √(x₁² + x₂²), and r₂ = √(x₃² + x₄²)). If r₃ = √(r₁² + r₂²), that's √(x₁² + x₂² + x₃² + x₄²). Why does this matter?

Fact 1 told us: the longer the sub-vector, the more tightly its norm concentrates around its expected value. We can graphically see this:

![Distributions visualized in Desmos](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774564674-hewowgrbaaas1m.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

At level 3, each radius summarizes 4. At level 4, each radius summarizes 8. And Fact 1 told us: the longer the sub-vector, the more tightly its norm concentrates around its expected value. A 2D norm can still vary a lot. An 8D norm barely varies at all. So when you divide two 8D norms, the ratio is extremely close to 1, and arctan is extremely close to 45°.

Level 3 pairs radii that are norms of 4D sub-vectors (d=4 curve, narrower, angles tighter). Level 4 pairs radii of 8D sub-vectors (d=8, even tighter).

Level 7 is a 128D vector, you're pairing norms of 64D sub-vectors. Basically constant at 45 degrees. Can be quantized with one bit / basically needs one bucket as they all map to same value.

This is what Lemma 2 captures. The distribution at level ℓ is:

The joint distribution of a Gaussian vector's polar angles factors into independent per-level distributions where level 1 is uniform, and levels 2+ follow sin^(2^(ℓ-1)-1) which peaks harder at π/4 with each level.

And here's the scary math that says this:

## The algorithm

First, we construct the rotation matrix. This part's simple enough. A random matrix, with Gram-Schmidt applied on top, is stored and reused across the board.

![Algorithm Part 1](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774564807-hexpw1ybyaed2do.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Use the rotation matrix to precondition, and then apply the polar transformation as shown in the figure above.

```
1    r = y.clone()
2    angles = []
3
4    for level in range(n_levels):
5
6        a = r[0::2]  # even indices: r^(ℓ-1)_{2j-1}
7        b = r[1::2]  # odd indices:  r^(ℓ-1)_{2j}
8
9        # ψ_j^(ℓ) = atan2(r_{2j}, r_{2j-1})
10        level_angles = torch.atan2(b, a)
11
12        if level == 0:
13            # l 1: raw coordinates can be negative [0, 2π)
14            level_angles = level_angles % (2 * np.pi)
15        # l 2+: radii are always positive
16
17        # r_j^(ℓ) = ||r_{2j-1:2j}||_2
18        new_r = torch.sqrt(a**2 + b**2)
19
20        angles.append(level_angles)
21        r = new_r  # carry radii to next level
22
23    return angles, r  # output r^(log2 d), ψ^(1)...ψ^(log2 d)
```
Then, we build our codebooks. What are these? Recall from lemma 2, our angles at each level follow a known distribution. This right here is the whole trick. All the math we did, was to get to a point where we can say:

I know the exact distribution my data (angles) will follow at each level. This means I know exactly where my optimal quantization buckets fall ahead of time. This means I can pay the price of online quantization once, offline, before any inference takes place. I will store my bucket values (centroids) in look-up tables, which I will keep on SMEM. When it is time to quantize, I'll simply look up the closest bucket.

```
codebooks = [
        build_codebook(n_bits=4, lo=0, hi=2*np.pi, level=0),  # level 1: 16 entries
        build_codebook(n_bits=2, lo=0, hi=np.pi/2, level=1),  # level 2: 4 entries
        build_codebook(n_bits=2, lo=0, hi=np.pi/2, level=2),  # level 3: 4 entries
        build_codebook(n_bits=2, lo=0, hi=np.pi/2, level=3),  # level 4: 4 entries
    ]
```
```
def build_codebook:
    exponent = (1 << level) - 1  # 2^(l-1) - 1
    sin2theta = torch.sin(2 * theta)
    angles_pdf = torch.pow(sin2theta.clamp(min=0), exponent)
```
We now have say 10k numbers, each one says how likely an angle will exist here. At π/4 it'll be high, else low (according to our lemma).

We then turn the PDF (probability density function) into a discrete probability distribution (by normalizing with the sum), and then turn that into a CDF (what percentage of angles falls here or before here)

```
 weights = weights / weights.sum()
 cdf = torch.cumsum(weights, dim=0)
 for i in range(n_codes):  # n_codes = 4 for 2 bits
     target = (i + 0.5) / n_codes  # 0.125, 0.375, 0.625, 0.875
     idx = torch.searchsorted(cdf, target)
     centroids[i] = grid[idx]
```
n_codes is the number of quantization buckets we have (2 raised to the quantization factor), and for all levels except the first it will be 4. This gives each bin roughly equal probability mass, assumes that all angles are uniformly distributed (we know this isn't true, and that they're clustered around π/4, but bear with me).

We run Lloyd's algorithm.

```
1for iteration in range(n_iters):
2    boundaries = torch.zeros(n_codes + 1)
3    boundaries[0] = lo
4    boundaries[-1] = hi
5    for i in range(1, n_codes):
6        boundaries[i] = 0.5 * (centroids[i-1] + centroids[i])
7
8    old_centroids = centroids.clone()
9    for c in range(n_codes):
10        mask = (grid >= boundaries[c]) & (grid < boundaries[c+1])
11        w = weights[mask]
12        if w.sum() > 1e-15:
13            centroids[c] = (w * grid[mask]).sum() / w.sum()
14
15    if (centroids - old_centroids).abs().max() < 1e-7:
16        break
```
We draw boundaries at midpoints between adjacent centroids (with the absolute low being 0, and the absolute high being 2π for level 0, or π/2 for subsequent levels, as discussed earlier).

We then recompute each centroid as the probability-weighted average of all points in its bin (so centroids get pulled toward the peak, not the geometric center), repeat until nothing moves. Out come 4 perfectly centered centroids.

Here's a visual:

![My artwork](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774564911-hew-hcqbyain06k.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

Just kidding. I would never. Here you go:

![Claude's translation of my artwork](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774564965-hexbtlma8aa8tx8.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

We KNOW all our angles (at this level) are going to be quantized to one of these 4 centroids. We're certain of this. So, we precompute cos and sin of each centroid. And that, is the codebook. A 4-entry lookup table.

```
cos_table = torch.cos(centroids)
sin_table = torch.sin(centroids)
```
and then we can actually quantize by mapping to closest centroid.

![Algorithm Part 3](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774565031-hexqdq1bqaaph61.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

If we take a closer look at our distribution of angles we genuinely see the number of angles spike at π/4.

![Distribution Visualized](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774565073-hewrkvjbyait6v2.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

This is why PolarQuant can design codebooks without seeing any data. After preconditioning, the angles only depend on the distribution of S·x, which is Gaussian regardless of what the original embeddings looked like. The relative error and dot product preservation is also perfect.

![Accuracy Visualized](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774565109-hewroc6byamcoc6.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

If we look closely, after encoding, each 128-dimensional token is stored as: 64 angle indices at 4 bits each (level 1, where angles span the full circle), 32 indices at 2 bits (level 2), 16 at 2 bits (level 3), 8 at 2 bits (level 4), and 8 leftover radii in full 16-bit precision. That's 256 + 64 + 32 + 16 + 128 = 496 bits per token. The original FP16 vector was 128 × 16 = 2,048 bits.

Compression: 4.13×

![Quantization Visualized](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774565158-hewrrgqawaalnmd.jpeg%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

## The code

This covers the theory. But how do we actually use this quantization scheme in practice, and how does it fare against cuBLAS matmul? The kernels (all created by agents using [@karpathy ](https://x.com/@karpathy)auto-tuning framework), yielded interesting results:

- The most optimized kernel could get ~75% the performance of cuBLAS at 65k and 512k sequence length.
- Any sequence length under 8K was bound by time it took to launch kernel, no difference here.
- CuBLAS is consistently ~50% better on everything else.

![Kernel Perf](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774565214-hewqcktbyaykpg1.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

![Kernel Benchmark](https://www.baseten.co/_next/image/?url=https%3A%2F%2Fwww.datocms-assets.com%2F104802%2F1774565248-hexyrpzbyaagt45.png%3Fauto%3Dformat%26w%3D1200&w=3840&q=75)

I think I could have squeezed more performance if I prompted harder, but I ran out of tokens and got a bit bored.

The code for the kernels is available here: [https://github.com/AliesTaha/polar_quant](https://github.com/AliesTaha/polar_quant)

## TLDR:

Is PolarQuant different from NVFP4? Yes. Three ways.

- NVFP4 stores per-block scale factors. PolarQuant does not. No overhead.
- NVFP4 uses uniformly spaced buckets. That's all it can do. Here, we account for a known distribution
- NVFP4 needs calibration data for PTQ to run offline quantization (you pay in quality degradation) or a runtime max-scan / online quantization (you pay in performance). PolarQuant precomputes everything analytically. A free lunch...almost.

A more optimized kernel is needed to make this competitive. 75% the speed of cuBLAS just won't cut it. Coming soon? We'll try to cook something here at Baseten.
