---
title: 'Write small, learn forever: rank-1 LoRA for continual learning'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/write-small-learn-forever
author: Charles O'Neill
published: '2025-10-12'
fetched: '2026-11-12T06:16:34Z'
classifier: null
taxonomy_rev: 2
words: 2728
content_sha256: e41583dcc04c7fde4d21632c95a19165d86fb9ff53f066a6f886f701a1aee7d4
---

# Write small, learn forever: rank-1 LoRA for continual learning

Research
# Write small, learn forever: rank-1 LoRA for continual learning

Why rank-1 LoRA updates might be the missing link between static fine-tuning and truly continuous, live-on-GPU learning.


- Authors
- Date
- October 12, 2025

TLDR

A caveat to start off this post: We actually don’t necessarily know if LoRAs are the right way to think about continual learning anymore. The point of us thinking about it in the first place was basically from an engineering perspective: how do you get a model which “feels” like it’s actually continuously updating, rather than being a static snapshot with these discrete fine-tuning runs you do? We wanted to make continual learning feel a lot more like prompting: if you had a certain learning signal that you trusted, or you wanted to tweak it or add new learning signals, you could see these changes immediately start to shape the behaviour of the model. Continuously (or close to continuously) merging rank-1 LoRA adapters into the model on the same GPUs running inference felt like the right answer to that to us. However, it doesn’t really solve a lot of the problems of continual learning. For instance, although LoRAs suffer from catastrophic forgetting less than full fine-tuning, we know it’s still a problem. It also doesn’t necessarily let you be as modular if you’re continuously merging them into the base model ie if you retained the individual LoRA (rather than having continuously refreshed ones that you keep merging), then you can do things like hot-swapping LoRAs on the same base model to make inference much more effective for multiple customers. This is one reason why we’re looking more towards things like CARTRIDGES and sparse memory fine-tuning, which we’ll talk about in future posts. I think the right way to think about this is that the stuff below would likely work well when your task distribution is stationary and is narrowly confined enough such that you can kind of “patch all the holes” through doing fine-tune updates over time. In addition to this, it probably relies on having examples (within the task) that are repeatable enough and similar enough to each other that there’s not going to be a massive “surprise” because someone suddenly asks who the POTUS was in 1972 and you’ve been writing clinical notes the whole time. (In general, I think catastrophic forgetting for specialised models is not as much of a problem as everyone makes it out to be; not that it doesn’t happen, but you don’t really care if your model remembers the years of Presidents if it’s never going to be relevant to the task at hand.)

What fascinated us earlier this year was this idea: what if models could feel a lot more alive, much like Dwarkesh’s intern, much like how prompting changes feel immediate? Not these static artifacts that get periodically retrained, but something that learns continuously, moment by moment, the way you might imagine human learning works. We wanted the experience of working with a model to feel less like swapping out snapshots and more like having a conversation with something that's actively incorporating feedback. You give it a learning signal you trust, maybe tweak it, add new signals, and you'd see these changes immediately start to shape the model's behaviour, rather than after some overnight training run, but right there, as you work with it.

This led us down a bit of a rabbit hole. We started thinking: okay, if we want to continuously merge rank-1 LoRA adapters into the model on the same GPUs doing inference, what does that actually mean mathematically? Can we even do this without everything falling apart?

When you train a neural network with stochastic gradient descent, you're already doing low-rank updates. Not approximately or effectively, but literally. Think about what happens when a single training example passes through a linear layer. You've got this transformation $h = Wx$ where $W \in \mathbb{R}^{m \times n}$ and $x \in \mathbb{R}^n$ is your input. During backprop, the loss $\ell$ sends back a signal $\delta = \partial \ell / \partial h \in \mathbb{R}^m$. The gradient with respect to the weight matrix becomes:

$$
G = \nabla_W \ell = \delta x^\top
$$

This is just an outer product—a rank-1 matrix. Every column of $G$ is a scalar multiple of $\delta$, every row is a scalar multiple of $x^\top$. Even with a mini-batch $({\delta_b, x_b})_{b=1}^B$, you're just summing these up:

$$
G_{\text{batch}} = \sum_{b=1}^B \delta_b x_b^\top
$$

I guess intuition says that restricting yourself to rank-1 updates should cripple learning (even though people have written about this being naturally low-rank before); after all, you're only pushing weights along a single direction. But if SGD is already doing this naturally, maybe we weren't restricting anything fundamental. Maybe we were just making explicit what the optimization process already wanted to do.

We kept wondering, if we're going to merge these rank-1 updates continuously, do we need to be super careful about when we merge? Like, what's the difference between accumulating a bunch of micro-updates and merging them all at once versus merging after each tiny step?

It turns out they're basically the same thing up to second-order terms. When each micro-loss $\ell_i(W)$ is L-smooth and your updates are small, you can expand the gradient via Taylor series. If $g_i(W) = \nabla \ell_i(W)$, then:

$$
g_i(W_{i-1}) = g_i(W) + H_i(W)[W_{i-1} - W] + O(|W_{i-1} - W|^2)
$$

Since the drift $W_{i-1} - W$ is itself $O(\eta)$, the correction per micro-update is $O(\eta)$. Multiplying by $\eta$ to get the actual step gives you $O(\eta^2)$. Summing over all steps, you get $|W_{\text{merge}} - W_{\text{acc}}|_F = O(\eta^2)$.

What this means in practice is that when you move the base weights by tiny amounts, the gradient at the next micro-step barely changes to first order. Whether you merge immediately or bundle updates, you get essentially the same answer.

Okay, but if you're only doing rank-1 updates, how do you ever learn anything complex? The answer lies in how these updates accumulate over time. Each micro-update can be written $\hat{\Delta}_t = \gamma_t \hat{u}_t \hat{v}_t^\top$ with unit vectors and magnitude $\gamma_t > 0$. After T merges:

$$
\Delta_{\le T} = \sum_{t=1}^T \gamma_t \hat{\Delta}_t
$$

The key insight is that the span of your updates grows as gradients naturally rotate through different directions. We started thinking about this through the lens of stable rank:

$$
\mathrm{srank}(\Delta) = |\Delta|_F^2 / |\Delta|_2^2
$$

If updates keep pointing in fresh directions (bounded coherence $\max_{s<t} |\langle \hat{\Delta}_t, \hat{\Delta}_s \rangle_F| \le \rho < 1$, then:

$$
\mathrm{srank}(\Delta_{\le T}) \gtrsim T / (1 + \rho(T - 1))
$$

When $\rho$ is small, stable rank grows roughly linearly with T. It's like you're painting a picture one brushstroke at a time; each stroke is simple, but they accumulate into something rich. The restriction is momentary; the capacity is cumulative.

This led us to think about what LoRA is actually doing geometrically. When you parameterise an increment as $\Delta W = AB^\top$, you're essentially solving a proximal problem:

$$
\min_{\mathrm{rank}(\Delta) \le r} \langle \nabla \ell(W), \Delta \rangle + \frac{1}{2\eta} |\Delta|_F^2
$$

The solution comes from the Eckart–Young–Mirsky theorem. If you decompose the gradient as $\nabla \ell(W) = \sum_j \sigma_j u_j v_j^\top$, the best rank-r approximation keeps the top r components:

$$
\Delta^* = -\eta \sum_{j=1}^r \sigma_j u_j v_j^\top
$$

For rank-1, you're literally just picking the single most important direction at each step. It's steepest descent in the geometry of the nuclear-norm ball rather than regular Euclidean space. There's something philosophically satisfying about this because you're not trying to do everything at once, just the most important thing right now.

Of course, not everything is this clean. The place where our beautiful continuous learning vision starts to get complicated is when you move from supervised fine-tuning to reinforcement learning.

In SFT with teacher forcing, your data $x \sim p_{\text{data}}$ doesn't depend on model weights. Update W mid-epoch, and your gradient still targets $\mathbb{E}{x \sim p_{\text{data}}}[\ell(W;x)]$. There's no notion of being “off-policy.” This is why our first-order equivalence holds completely, because the data distribution stays fixed regardless of when you merge. This is where you really get that magical "feels like prompting" experience we were after.

But in on-policy RL, your data $tau \sim p(\tau | \pi_W)$depends directly on W. If you merge updates during rollout collection, you're changing the policy generating later trajectories. Now you need importance weights:

$$
\prod_t (\pi_W(a_t|s_t) / \pi_{W_t}(a_t|s_t))
$$

There's also this striking difference in information density that we kept coming back to. In SFT, a sequence of length T with cross-entropy b bits per token gives you roughly bT bits of training signal. In terminal-reward REINFORCE, an entire episode might communicate less than one bit about the first decision. This actually explains something we'd noticed empirically ie rank-1 often matches full fine-tuning in RL not because it's equally expressive, but because the supervision channel itself is the bottleneck (also heaps of other people have talked about [this](https://thinkingmachines.ai/blog/lora/)).

But really the hardest thing is managing the optimizer. Using Adam for continuously merging LoRAs in this fashion is non-trivial because Adam's updates are guided by the first and second moments accumulated over previous steps. After you merge a LoRA adapter and initialize a fresh one, if you keep using the old gradient moments, they'll push the new adapter in the same direction as the previous one ie you end up optimizing the same subspace repeatedly. [ReLoRA](https://arxiv.org/abs/2307.05695) tackles this with a partial reset of the optimizer state through magnitude pruning, zeroing out the learning rate with a warm-up to prevent the loss from exploding, and even requiring a short full-rank warm-start when training from scratch. This is probably the biggest engineering headache in making this stuff actually work.

We kept coming back to this engineering reality: what does it actually mean to run continuous learning on the same GPUs serving production traffic? This is where rank-1 LoRA starts to look less like a nice mathematical property and more like the only thing that could possibly work.

Think about the memory constraints first. Full fine-tuning needs optimizer state for every parameter—with Adam, that's roughly 3× the model size. For a 70B model, you're looking at 210B parameters worth of optimizer state alone. Rank-1 LoRA per layer? You're storing just $A \in \mathbb{R}^{m \times 1}$ and $B \in \mathbb{R}^{n \times 1}$ plus their tiny optimizer states. Memory scales as $O(m+n)$ instead of $O(mn)$.

But here's where we had to get precise about what "continuous updating" actually means. There are two totally different operations that we kept conflating at first:

**Hot-swapping adapters is the instant gratification part.** You keep the adapters factored and compute $Wx + B(Ax)$ at inference, and the cost is just $O(r(d_{in} + d_{out}))$ extra ops per token, which with $r=1$ is basically nothing. These A, B tensors are so small you can atomically swap pointers between requests with microsecond-scale locks. Broadcast the new tensors across your tensor-parallel shards once, without gigabyte copies and repacking. This is how you get that immediate “the model just learned something” feeling without touching the base weights at all.

1. **Actually merging is different.** Adding $AB^T$ into W means touching $O(mn)$ elements per matrix—you're doing this for Q/K/V/O and MLP layers across all shards. It's bandwidth-bound, not compute-bound, and definitely not free. If you're running quantised (which, let's be honest, you probably are), you either dequantise-add-requantise or maintain a high-precision delta buffer that gets folded in during periodic requantisation.

So the production pattern we started imagining looks like this: serve with factored adapters for immediate effect. Accumulate gradients on those adapters right on the serving GPUs. When you've got a moment (low load, or on a shadow replica) run the actual merge using fused rank-1 kernels. Roll traffic to the merged version. Keep a ring buffer of recent deltas for rollback.

Picture it: 8 H100s serving your model, each shard keeping a few kilobytes of adapter parameters pinned in HBM. User interactions immediately update these tiny adapters via NCCL broadcast. Every few seconds, or when load dips, you pick a shadow replica, apply the rank-1 update to its weights (respecting quantisation), smoke test, and flip traffic. From the outside, the model just seems to be getting smarter continuously. You can change your learning signals (swap reward functions, adjust your LLM-as-judge) and feel the model start responding differently almost immediately through the adapter path, which is just so cool to think about.

There's something elegant about checkpointing here too. Ring-buffer the last K rank-1 updates with metadata about what produced them. Something goes wrong? Roll back merges. Want to understand why the model changed? The provenance is right there, not in some terabyte checkpoint graveyard.

The reality check is that companies like Cursor already redeploy [every two hours](https://cursor.com/blog/tab-rl), which is incredible engineering. But what we're sketching is qualitatively different ie behaviour changes immediately via adapters, persists via background merges, and the serving fleet just keeps humming. It's learning that feels continuous because it actually is continuous, with updates flowing as naturally as forward passes.

There's this whole question of capacity that kept nagging at us. People talk about parameter counts, but that feels like the wrong lens. If you train on N tokens at b bits per token, you can't extract more than bN bits of generalisable information. A rank-1 LoRA across all projections of a modern model is millions of parameters. Even at 1–2 bits of information per parameter, that's massive headroom for most continual learning scenarios.

We also played around with LoRA-XS, which takes a different philosophical stance. You approximate W via truncated SVD as $W \approx U_r \Sigma_r V_r^\top$ and learn just a small core matrix $R \in \mathbb{R}^{r \times r}$. The updates become $\Delta W = U_r R V_r^\top$. It's incredibly parameter-efficient, just $r^2$ parameters—and great for composition. But you lose that span growth we talked about. Your reachable span is frozen to what the pre-trained weights already encode. Whether that's a feature or a bug depends on your use case. But we’ve [found](https://www.baseten.co/resources/research/practical-lora-research/) it doesn’t work that well.

As for convergence, in convex settings you can view rank-1 LoRA through Frank-Wolfe optimization on the nuclear-norm ball—you get $O(1/t)$ convergence. For the non-convex networks we actually care about, with appropriate step sizes you still get:

$$
\min_{t<T} |\nabla \ell(W_t)| = O(1/\sqrt{T})
$$

Nobody's claiming you'll land at exactly the same minimizer as full fine-tuning, but you reach a comparable stationary point.

Dwarkesh raised an [interesting point](https://x.com/dwarkesh_sp/status/1962253189878858148) recently, comparing bytes in KV cache versus LoRA adapters, noting that at 100k tokens you get 37× “compression” and wondering if this meant LoRA couldn't match in-context learning's richness. But this comparison tracks the wrong thing entirely. KV cache is read memory: transient, lossless storage that grows linearly with tokens so attention can query any context. LoRA is write memory: a fixed, tiny set of weights storing generalizations that gradient descent has distilled. Comparing their bytes per token is like comparing the size of your desk to the size of your brain, because they serve fundamentally different purposes.

The real question isn't “how many bytes per token” but “how many bits of generalizable signal does a session provide?” In supervised fine-tuning, a sequence of length T at b bits/token carries up to bT bits of learning signal. In binary RL, an entire episode might communicate one bit (it’s a bit handwavy, some of these information theoretic arguments, but we move). Most sessions contain far fewer bits-that-matter than the raw token count suggests: a rule to forbid, a corrected schema, a preferred template, compact invariants. A rank-1 LoRA across all projections has millions of parameters, massive headroom for these bits. The bottleneck is almost never adapter capacity; it's the rate at which you extract useful signal from your data stream. And importantly, unlike KV cache which vanishes between sessions, those learned bits persist forever, which is the one thing in-context learning cannot give you.

**For attribution in academic contexts, please cite this work as:**

*O'Neill, Charles, Max Kirkby, Harry Partridge, and Jonathon Liu. "Write Small, Learn Forever: Rank-1 LoRA for Continual Learning." Baseten Research, October 12, 2025. https://www.baseten.co/research/write-small-learn-forever/*

**BibTeX citation**

```
@misc{oneill2025lora,
  author       = {O'Neill, Charles and Kirkby, Max and Partridge, Harry and Liu, Jonathon},
  title        = {Write Small, Learn Forever: Rank-1 {LoRA} for Continual Learning},
  year         = {2025},
  month        = oct,
  day          = {12},
  howpublished = {Baseten Research},
  url          = {https://www.baseten.co/research/write-small-learn-forever/},
}
```
