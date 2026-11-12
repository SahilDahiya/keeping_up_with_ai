---
title: The platform for inference, training, and execution | Baseten
kind: blog
topic: models
subtopic: fine-tuning
secondary_topics: []
summary: Replicates Generative Adversarial Distillation (GAD), distilling Qwen3-4B
  from GPT-5.2 outputs alone (no logits/hidden states) using an on-policy discriminator
  trained in parallel with the student on 8xH200s over ~10 hours on 20K examples,
  avoiding the distribution-shift failure mode of plain sequence-level distillation.
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/distillation-without-the-dark
author: Max Kirkby
published: '2026-02-11'
fetched: '2026-11-12T06:15:52Z'
classifier: claude
taxonomy_rev: 2
words: 1952
content_sha256: f99c75d5a14b4f0629c72013bdbbeecbde724dc48ebfa76e87db4048d053991a
---

# The platform for inference, training, and execution | Baseten

Research
# Distillation without the dark

Replicating black-box on-policy distillation on the Baseten stack


- Authors
- Date
- February 11, 2026

TLDR

In the following post, we replicate the results of Ye et al. (Microsoft Research), who introduced a method of LLM distillation via Generative Adversarial Distillation (GAD). GAD is a method of adversarial distillation where the discriminator is an on-policy reward model able to co-evolve with the student (learning) model, circumventing typical issues with supervised fine-tuning on pure teacher responses. Here, we distill Qwen3-4B (student) from GPT-5.2 using 8xH200s using the Baseten Training product, training in \~10 hours on 20K examples. We show that the method works: the discriminator learns to separate teacher from student during warmup, and the student successfully learns to fool it during adversarial training without collapsing or length hacking.

**Why black-box distillation doesn't work**

Say you want to distil a closed-source model like GPT-5.2 into an open-source model that you could run on your own stack. You run into an immediate problem: you don’t have the necessary inputs to train a viable model. Distillation in this paradigm requires a process that runs without logits, hidden states, or attention patterns. Just text. So what do you do? The *current* approach is embarrassingly simple. Collect a bunch of (prompt, teacher response) pairs and fine-tune a student model to imitate these responses with plain next-token prediction. [Sequence-level knowledge distillation (SeqKD)](https://arxiv.org/abs/1606.07947), as it's called, just teaches your model to copy the teacher. At inference time the student must generate autoregressively from its own prefixes, which diverge from the teacher's. This is a form of distribution shift where small prediction errors compound over the sequence as the student moves further off the expert distribution it was trained on, a failure mode well-characterized in imitation learning. **Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "efPetwL4Q1iiYzaHTfq8sg"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "efPetwL4Q1iiYzaHTfq8sg"
  }
}

Separately, white-box distillation goes one step further, computing KL divergence on student-generated text. This is where the student samples from itself and then the teacher provides supervision at what should have been done at each step. As always however, there's a catch. When your teacher is a closed-source model, you can't compute **Placeholder: ContentMathRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "frvTsfeSTrueDf\_EPCvCqA"
  },
  "record": {
    "\_\_typename": "ContentMathRecord",
    "id": "frvTsfeSTrueDf\_EPCvCqA",
    "formula": "KL(p(⋅∣x)∥qθ(⋅∣x))"
  }
}token-wise because you don't have *p* (the teacher's conditional distribution over next tokens).**Placeholder: ContentFootnoteRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "IET7DkIeTm-WGift69gOsg"
  },
  "record": {
    "\_\_typename": "ContentFootnoteRecord",
    "id": "IET7DkIeTm-WGift69gOsg"
  }
}

Distillation is therefore stuck with a supervision problem: "this is what a good response looks like", with very little information about why this particular response is good. This framing is perhaps similar to our previous posts on [iSFT](https://www.baseten.co/research/iterative-sft/) and [RGT](https://www.baseten.co/resources/research/upweight-the-strategy-not-the-tokens-faster-training-with-explicit-reasoning-thro/), whereby different training signals yield differing amounts of information. In this case, current methods of distillation are impoverished.

With these problems in mind, Ye et al. introduced Generative Adversarial Distillation (GAD).**Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "OkWcMPwPSl2111WkfkkPYw"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "OkWcMPwPSl2111WkfkkPYw"
  }
}  Here the authors reframe this supervision problem as a reward modelling problem, by simply training a discriminator to tell us whether a student's generation is teacher-like. Get the discriminator good enough to distinguish teacher from student outputs, and then optimize the student to fool it. In doing so, the discriminator becomes an on-policy reward model that provides feedback on the student's own generations.

**Constructing an on-policy reward model**

GAD frames distillation as a two-player minimax game. The student (generator) produces responses to prompts and a discriminator learns to distinguish student from teacher outputs. The discriminator is initialized from the generator's model parameters (in our instance, this is (Qwen3-4B) and augmented with an additional prediction head that projects the final hidden state to a scalar score. The score of the last token in the sequence is taken as the sequence-level score. The generator is then optimised to produce responses the discriminator can't tell apart from the teacher's. The value function for this game is:

$$
\max_G \min_D \mathbb{E}_{(x, y_t) \sim \mathcal{T}} \left[ -\log \sigma\big(D(y_t) - D(G(x))\big) \right]
$$

where $x$ is the prompt, $y_t$ is the teacher response, $G(x)$ is the student’s generated response, $D(\cdot)$ is the discriminator’s scalar score, and $\sigma$ is the sigmoid function.

Ye. et al. train the discriminator with a Bradley-Terry pairwise loss. Given a prompt, a teacher response, and a student response, the discriminator assigns scalar scores to each and is trained to score the teacher higher:

$$
\min_D \mathbb{E}_{(x, y_t) \sim \mathcal{T}} \left[ -\log \sigma\big(D(y_t) - D(G(x))\big) \right]
$$

This is the same as classical RLHF, but instead of learning human preferences we're detecting likeness to a teacher model. The generator then treats this discriminator score as a reward signal and seeks to maximize it: 

$$
\max_G \mathbb{E}_{(x, y_t) \sim \mathcal{T}} \big[ D(G(x)) \big]
$$

The key trick that Ye et al. introduce here is that the discriminator updates during training, thus getting an adaptive reward signal and avoiding reward hacking (on static data a fixed reward model could just find outputs that score highly). Hence, the discriminator and generator co-evolve, yielding a student that gets better at fooling the discriminator and a discriminator that gets better at detecting fakes.

This is analogous to the minimax game in GANs, where the global optimum is reached when the generator matches the data distribution and the discriminator converges to chance-level accuracy (goodfellow citation). This co-evolutionary, on-policy structure also appears in recent self-distillation work: Zhao et al. show that a model can serve as both teacher and student by conditioning on privileged information, replacing the discriminator with a KL-based distillation loss while retaining the insight that adaptive supervision on the student's own generations outperforms just imitation.**Placeholder: ContentFootnoteRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "IoKn4vhZSv6BRwIFcM6yCw"
  },
  "record": {
    "\_\_typename": "ContentFootnoteRecord",
    "id": "IoKn4vhZSv6BRwIFcM6yCw"
  }
}

The generator and discriminator updates are also not strictly 1:1. The discriminator is updated online after accumulating a batch of rollouts. In our case, we generate 8 student samples per prompt, obtain 8 rewards, and perform 1 discriminator update. This follows the GRPO implementation described by Ye et al.

A note here on warmup (we show our results on this later). If we start the mini-max game from scratch, we get trivial separation of teacher from student. With the student obviously worse than the teacher initially, the generator gets no useful gradient and can't improve. Similarly, if the generator is far stronger than the discriminator, the discriminator struggles to tell apart teacher vs student responses. The fix to this is to therefore warm up both models prior to true adversarial training: SFT the generator on teacher responses (standard seqKD) and then simultaneously train the discriminator to separate teacher from student.

**A replication experiment**

We replicate GAD on Baseten infrastructure, distilling Qwen3-4B from GPT-5.2 on 8xH200s. Our dataset consists of \~20K (prompt, teacher response) pairs, where teacher responses are sampled from GPT-5.2 with a 1536 token output cap. We matched the core structure of Ye et al., using a discriminator bootstrap (10 steps of discriminator loss with generator frozen), a joint warmup (generator cross-entropy and discriminator for 100 steps) and then the full GAD run. Compared to Ye et al., who distill Qwen2.5-14B on 200K examples across 16xH100s in 30 hours, our smaller-scale setup (Qwen3-4B, 20K examples) fits the full training pipeline on 8 H100s in \~10 hours, with tweaked prompt/response sampling and batch sizing to optimize KV-cache memory and discriminator activations when both models are active simultaneously.

We deviate further from Ye et al. in introducing two further architectural changes. First, during the GAD stage we freeze the discriminator backbone and only update the attached linear head (that scores the last token's hidden state). This keeps discriminator updates cheap enough to stay on-policy. Second, we introduce a warmup sampling cap to the longest teacher response in the batch (plus a small margin) that prevents the student from 'winning' early on by just padding answers. Whilst we haven't validated the explicit utility of these changes, we find that they allow robust and efficient on-policy training on 8xH200s.**Placeholder: ContentFootnoteRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "bBmiiGFBQFCynxbtaHuByQ"
  },
  "record": {
    "\_\_typename": "ContentFootnoteRecord",
    "id": "bBmiiGFBQFCynxbtaHuByQ"
  }
}

In our experiments, we track two things: whether the discriminator stays calibrated during training, and whether the student actually improves beyond the warmup phase.

**Warmup dynamics**

We first conducted a joint warmup phase over 110 steps (Figure 1 below). The first 10 steps are a discriminator bootstrap, where the generator is frozen and only the discriminator trains to separate teacher from student outputs. The remaining 100 steps are joint warmup, where the generator trains with cross-entropy on teacher responses while the discriminator continues learning to distinguish between them. This replicates Ye et al.

In doing so, we observe a steady reduction in discriminator loss (a), indicating that the discriminator is learning to separate teacher from student. Similarly, the margin of these 'victories' (b) begins negative (preferring student, guessing wrong) and climbs to reliably prefer the outputs of GPT-5.2. The accuracy of judgments (c) tracks this. By the end of this warmup phase, the discriminator can thereby tell teacher from student well enough to provide a meaningful reward signal for the generator to optimize against in the adversarial phase.

**RL training**

We then run the full adversarial phase for 2400 steps (Figure 2). The discriminator reward (a) increases steadily, indicating the student is successfully learning to fool the discriminator (the outputs are increasingly scored as teacher-like). Indeed, this gradual improvement suggests that the discriminator and generator co-evolve stably. Policy entropy (b) decreases gradually as the student learns what 'teacher-like' looks like, without detectable mode collapse. Similarly, trainer-inference KL (c) is largely within limits and does not exhibit divergence from the reference policy.

Finally, completion length (d) remains stable throughout. This is exciting as it suggests that the student model is not reward hacking by padding outputs. This confirms that the student is producing teacher-like content.

**Evaluations**

To measure whether the student actually got better at the task (rather than just fooling our discriminator), we use an LLM-as-a-judge setup similar to Ye et al. For each prompt, we take model outputs and score them with GPT-4o for consistency, accuracy, and relevance. We observe that our GAD-trained model scores higher (a) and consistently (b) beats the warmup-only baseline. The teacher model (GPT-5.2) still scores higher, in line with distilling a 4B model from a much larger one. These results appear comparable to Ye et al.'s findings on Qwen2.5-3B-Instruct distilled from GPT-5-Chat (45.8 baseline, 48.9 trained, 51.7 teacher), evaluated using a normalized ratio from a GPT-4o reference scoring system.

**What's next?** Our work at Baseten is driven by continuous experimentation in post-training, where probing methods like GAD help surface new infrastructure patterns and training methodologies.

We believe an exciting extension to this replication is self-distillation. That is, can a model teach itself without an external teacher? Recent work from Zhao et al. on On-Policy Self-Distillation suggests that conditioning a model on privileged information and using it to supervise its unprivileged self can eliminate the need for an external teacher model.**Placeholder: ContentReferenceRecord (inlineBlock)**{
  "node": {
    "type": "inlineBlock",
    "item": "SWfoYKI-SDm\_FrlQoAJI0A"
  },
  "record": {
    "\_\_typename": "ContentReferenceRecord",
    "id": "SWfoYKI-SDm\_FrlQoAJI0A"
  }
} We're exploring whether this can deliver comparable gains to GAD and further enhance the efficiency and accuracy of on-policy distillation.

**For attribution in academic contexts, please cite this work as:**

*Kirkby, Max, Charles O'Neill, and Mudith Jayasekara. "Distillation without the Dark." Baseten Research, February 11, 2026. https://www.baseten.co/research/distillation-without-the-dark/*

**BibTeX citation**

```
@misc{kirkby2026distillation,
  author       = {Max Kirkby and Charles O'Neill and Mudith Jayasekara},
  title        = {Distillation without the Dark},
  year         = {2026},
  month        = {February},
  day          = {11},
  institution  = {Baseten},
  howpublished = {\\url{https://www.baseten.co/research/distillation-without-the-dark/}},
  note         = {Baseten Research}
}
```
