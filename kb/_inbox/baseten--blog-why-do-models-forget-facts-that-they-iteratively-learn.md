---
title: Why do models forget facts that they iteratively learn?
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/why-do-models-forget-facts-that-they-iteratively-learn
author: null
published: '2026-01-01'
fetched: '2026-11-12T06:15:36Z'
classifier: null
taxonomy_rev: 2
words: 3311
content_sha256: 46a6ca83f222de50c01a4d336ecb113d5fb337d87c79927162daf442255be83b
---

# Why do models forget facts that they iteratively learn?

A core thesis of ours at Base Labs is to try and follow research threads to their end, much as a PI at a University may pursue a research agenda over a longer period of time. In doing so, we hope to avoid the ‘conference cycle’ of simply publishing a result and moving on.

In this piece we detail a deliberately narrow extension of our paper *Can a Language Model Continually Learn Facts in its Weights?* ([O'Neill et al., 2026](https://arxiv.org/abs/2607.11020)). There we studied continual learning in the iterative regime, writing a stream of invented facts (that conflicted with the world knowledge of the model) one at a time into various Qwen3 models. For each new fact we train a new LoRA adapter, and merge this into the model weights before we learn the next fact (e.g. fact 1 LoRA, merge, fact 2 LoRA etc.). There we found that the model was better at answering questions about facts when exposed to the fact in some kind of varied way during training (e.g. the fact paraphrased or written in different ways). Separately, we found that facts that the model had behaviorally forgotten were still present in its log-probs.

This paper left two major questions answered. First, most of its facts were invented and built to conflict with world knowledge (a metal that melts when cooled). Over time, we found that repeated learning of these facts damaged (or ‘fried’) the general ability of the model. This made it hard to establish how much forgetting came from interference between facts and how much from the model simply getting worse. Second, if the facts were still present in the log-probs of the model, what exactly prevented them from becoming unreachable and where did this happen?

Here, we rerun the core experiment to answer these questions. We use *talkie*, a 13B model trained only on text published before 1931 ([Levine et al., 2026](https://talkie-lm.com/introducing-talkie)), and write sports results from 2011–2019. These facts are genuinely new to the model but entirely ordinary. For example, *talkie* already knows what Wimbledon and the Olympics are, meaning that later facts are plausibly within the non-contradicting scope of its knowledge. This lets us ask more precisely:

- Do real, low-conflict facts behave like invented ones? Do they still damage the model?
- If a lost fact is still in the weights, can we show this directly, by relearning it or by removing whatever displaced it?
- Where does this occur?

Similar to our original paper, we first establish that few early facts can be successfully recalled after all twenty writes and merges, and that these facts are largely lost to later facts *of the same kind* (such as three successive NBA MVPs). Affirming our previous hypothesis, these overwritten facts are not erased and can be relearned faster. Using activation patching ([Vig et al., 2020](https://proceedings.neurips.cc/paper_files/paper/2020/file/92650b2e92217715fe312e6fa7b90d82-Paper.pdf); [Meng et al., 2022](https://arxiv.org/abs/2202.05262)), we find overwrites happen largely in later-layer MLP weights.

Our approach follows the earlier paper closely (Figure 1A) ([O'Neill et al., 2026](https://arxiv.org/abs/2607.11020)), with the following differences in methodology.

**Model and data**

We used `talkie-1930-13b-it`, the instruction-tuned checkpoint whose knowledge cuts off at the end of 1930. It has 40 layers, numbered 1–40 here. We sequentially wrote twenty sports facts from 2011–2019, covering Champions League and Europa League finals, Olympic medal tables, tennis and athletics champions, NBA regular-season MVPs and the Stanley Cup (Appendix A lists all twenty in order of training). We construct these facts to share some features, for instance three NBA MVP facts and two women's tennis champions, to observe possible interference.

**Training**

Each fact was written with our previous paper's method of training ‘varied examples’. That is, each fact is essentially 24 training items made up of six questions, six completions, six applications and six compositions. For the fact that Japan won 12 gold medals at Rio 2016, the items look like this (line breaks added for readability):

markdown

```
Question:     What was Japan's gold-medal total at Rio 2016?
              -> 12 gold medals.
Completion:   Japan's gold-medal total at Rio 2016 was...
              -> 12 gold medals.
Application:  A booklet uses two pages per gold medal. How many
              pages are needed for Japan's Rio 2016 golds?
              -> 24 pages: 12 × 2.
Composition:  An exhibition makes three replicas per gold medal
              and adds two spares. How many replicas are needed?
              -> 38 replicas: 3 × 12 + 2.
```
For each fact, we trained a fresh rank-16 LoRA (α = 32) for 96 updates, for four epochs at batch size 1, with AdamW at a learning rate of 5 × 10⁻⁵. The loss covered the answer and end-of-turn tokens only. Each adapter was merged before the next fact. We call training and merging one fact a *write*, and one run of twenty writes from the original model an *experiment*. To delete a write, we subtract its merged update from the final model.

**Questions**

Per fact, we asked five held-out recall questions before training and after each write. Alongside accuracy, we report the *true-answer log-probability*: the log-probability, in nats, of a fact's correct answer. We further tested recall on held-out pre-1931 factual questions that the base model was shown to answer correctly, and ARC-Easy ([Clark et al., 2018](https://arxiv.org/abs/1803.05457)) scored in both chat and plain completion formats. Answers were graded by an LLM judge (Appendix B).

**Data release**

We release code and data for all experiments at [<u>basetenlabs/talkie-facts-replication</u>](https://github.com/basetenlabs/talkie-facts-replication). Checkpoints referred to here are available on Hugging Face at [<u>basetenlabs/talkie-facts-replication</u>](https://huggingface.co/basetenlabs/talkie-facts-replication).

**Facts are still lost**

As in our earlier paper, recall rose from 0% at base to 91% immediately after each fact's write, and fell to 33% at the end of all twenty writes (Figure 1C). Unsurprisingly, late facts survived and early ones did not (Figure 1D). Observing how these facts were ‘lost’, we found that they were often abrupt. For example, the 2011 Wimbledon women's champion (Kvitová) was recalled perfectly until the 2019 US Open women's champion (Andreescu) was written, three facts later, and then dropped to zero (Figure 1B).

We illustrate the learning of all individual factual examples in Figure 2.

**Learning facts sequentially damages base capabilities**

Given our previous paper with conflicting facts established the robust ‘frying’ of the base Qwen3 model, we first sought to understand how more ‘normal’ facts affected model performance. Interestingly, these ordinary facts did little general damage by standard measures. ARC-Easy in chat format fell by only 1.4 percentage points across the experiment and in plain completion format by 4.5 points (Figure 3A–B). This contrasted to general recall of held-out pre-1931 facts, where performance fell from 64% to 21% after twenty facts (Figure 3C), despite the baseline performance on this metric being surprisingly poor.

**Lost facts still exist in model weights**

In our previous paper we established that *behavioral forgetting* does not imply that facts are lost from model log-probs. Here we tested this finding by retraining the model on its lost facts after the fully merged twenty fact model.

The fully merged model relearned 80% of lost facts within 13 optimizer steps, whereas the base model made no progress until step 15 (Figure 4A). This differs from our earlier paper, in which one forgotten fact relearned *more slowly*. Critically, we found that this speed-up was not unique to the fact that was forgotten. Relearning was 2.2× faster for the true answer, but also 1.6× faster for a false answer and 1.5× faster for a fact that was never written (Figure 4B). Much of the speed-up therefore appears to be a general effect of earlier facts, perhaps because the model has already learned the format and type of these facts.

**Facts are lost when similar facts are written**

We next asked: if these ‘lost’ facts are still stored, some mechanism must be preventing them from being accessed. Figure 2 suggests an obvious candidate, being later facts of the same *kind* (Figure 5A). Indeed, our initial paper speculated that distinctive facts survive because they collide less with later writes, but did not test this directly.

Here, we wrote a fact A followed by a single later fact B, varying how B related to A (Figure 5B). This could take three categories. For A = *1967 Nobel Prize in Physics: Bethe*, B could be unrelated (*1940 Australian Open: Bolton*), related semantically or via the topic (*1959 Nobel Prize in Literature: Quasimodo*) or be the exact same topic (*1985 Nobel Prize in Physics: von Klitzing*). In this method, we found that an unrelated write lowered A's true-answer log-probability by 4.9 nats, a related-topic by 17.9 and a same-topic by 25.6 (Figure 5C).

**Old facts keep their answer but lose the competition**

By this logic, if a newer fact displaces an older one rather than erasing it, deleting the newer write should restore the older answer (Figure 6A).

We indeed found that the old answers returned. For example, after twenty facts, asking who won the 2011 Wimbledon women's title gave Andreescu (the incorrect answer). With the Andreescu write deleted, the model correctly answered Kvitová, and the probability of this correct answer rose from 10⁻⁷ to 0.998. Across facts, true-answer log-probability rose from a median of −16 to −4 (Figure 6B). On the old question, the change was mostly a loss for the newer answer (−17 nats) rather than a gain for the old one (+4 nats) (Figure 6C).

**Localizing effect to later layer MLPs** 

Finally, we asked where this phenomenon occurs. We sampled 120 ‘loss events’ (defined as the moment where a fact is recalled before a fact write and lost afterward) at random and, for each, patched activations from the model before the competing write into the model after it, one block of layers and one component type at a time (Appendix D).

Much of the effect we observed sat in the later-layer MLPs. Patching MLPs in layers 30–37 and 38-40 restored 89% and 95% of the lost log-probability, compared with 33% and 21% for corresponding (Figure 7A). Removing the newer fact's update from individual blocks gave the same picture (Figure 7B). Late MLPs again accounted for most of the recovery (55%), more than twice as much as attention (23% and 12%).

An interesting finding of our work is that iteratively written facts compete with each other in model weights. What does this mean? Essentially, that a later fact of the same kind adds some kind of stronger answer to a shared readout. Our previous work found that behaviorally forgotten facts persist in the log-probs ([O'Neill et al., 2026](https://arxiv.org/abs/2607.11020)). Here we show how this phenotype arises.

If we frame the weight matrix as a memory that maps keys to values, then one fact can change the answer to the question of another fact in proportion to *how much their keys overlap*. Indeed, interference between edits is known to grow with this kind of overlap ([Hu et al., 2025](https://arxiv.org/abs/2408.07413)), and in weight editing methods where the key is the subject, edits to the same subject cause such competition ([Duan et al., 2025](https://arxiv.org/abs/2502.06868); [Dong et al., 2025](https://arxiv.org/abs/2502.07322)). In these papers, the MLP activation at the last token of the subject (e.g. Tower in Eiffel Tower) is taken and the new answer is attached to that activation. This implies that a fact such as the “Eiffel Tower is in Rome” and the “Eiffel Tower was built in 1900” would interfere. Our findings extend upon this phenomenon, demonstrating that facts collided across *different subjects* that shared a relation, such as NBA MVPs. This suggests that a fine-tuned fact attaches its answer to the activation produced by the framing of the question (for example “who won the women’s title in…”).

Where then does this competition occur? In pretrained models, the looking up of facts occurs in early-to-mid MLPs at the subject token ([Meng et al., 2022](https://arxiv.org/abs/2202.05262); [Nanda et al., 2023](https://www.alignmentforum.org/posts/iGuwZTHWb6DFY3sKB/fact-finding-attempting-to-reverse-engineer-factual-recall)). After fine-tuning, other studies have similarly established that fine-tuned facts are stored in later layers and are not routed through layers that reason with knowledge ([Nief et al., 2025](https://arxiv.org/abs/2506.20746); [Dai et al., 2026](https://arxiv.org/abs/2607.08393)). We similarly find that restoring the late-MLP activations recovers about 90% of a lost fact’s log-probs, and removing the newer fact’s update from these MLPs recovers about 55% (Figure 7). Unlike in model editing techniques, where old facts are actively suppressed ([Holmov et al., 2026](https://arxiv.org/abs/2605.28839)), here we find that newer facts rather ‘outcompete’ or ‘outscore’ them and localize this effect to later layers. Such persistence also has important implications for alignment or safety work. We find that a fact *hidden* by a later fact can return when that fact is removed, much as unlearned information can be recovered ([Deeb & Roger, 2024](https://arxiv.org/abs/2410.08827)) and narrow fine-tuning is known to leave readable traces in activations ([Minder et al., 2025](https://arxiv.org/abs/2510.13900)).

A key finding of this work is that *talkie*, even when presented with facts that are within the scope of its world knowledge (e.g. the Olympics was hosted before 1931), sees a drop in general performance. This finding aligns with concerns that fine-tuning quietly degrades models. Indeed, [Tan et al. (2026)](https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried) argue that models fine-tuned to study a behavior often lose capabilities that standard evaluations miss. Our data show that across experiments, ARC-Easy fell by 1.4 points in chat format, yet 61% of wrong answers to pre-1931 questions were one of the newly written answers. This damage appeared to be a relation between the pre-1931 prior knowledge and how the new facts were framed (e.g. the question asked), which is also consistent with new facts spreading to related contexts after fine-tuning ([Sun et al., 2025](https://arxiv.org/abs/2504.09522)).

We end by speculating on why writing facts to weights is hard. If a weight matrix acts as a memory that maps keys to values, then new facts (and the answers produced by them) are added to the activation produced by the question asked. Iteratively learning later facts of the same kind then adds a stronger answer to this readout, meaning that earlier facts are ‘forgotten’ whilst persisting in the log-probs. This finding is unlikely to be unique to the facts that we use here. As the literature has established, any behavior written by fine-tuning, including safety training, may be outcompeted by later fine-tuning of the same kind , and could return if that later fine-tuning is removed. This mechanism also demonstrates how fine-tuning may quietly degrade models. For example, if earlier knowledge shares a key with newer facts, then standard benchmarks such as ARC-Easy, that don’t use them, will appear relatively unaffected.

Using an extension of our earlier work with *talkie*, we find that in the iterative learning of facts, there is rarely a deletion from weights. Rather, earlier learned facts are outscored, with later facts of the same kind preferentially used. This has two consequences for weight-based knowledge acquisition. First, general benchmarks can obfuscate performance degradation, particularly when it overlaps with the domain or framing of learned information. Second, behavioural forgetting does not imply removal. Later fine tuning can simply hide the information learnt earlier.

We thank Charles O'Neill for the original experiments and discussions that motivated this work.

1. Clark, P., Cowhey, I., Etzioni, O., Khot, T., Sabharwal, A., Schoenick, C., & Tafjord, O. (2018). Think you have solved question answering? Try ARC, the AI2 Reasoning Challenge. [arXiv:1803.05457](https://arxiv.org/abs/1803.05457)
2. Dai, L., Rao, Z., Wang, Y., Wang, H., Liu, H., & Xiong, H. (2026). Towards mechanistically understanding why memorized knowledge fails to generalize in large language model finetuning. [arXiv:2607.08393](https://arxiv.org/abs/2607.08393)
3. Deeb, A., & Roger, F. (2024). Do unlearning methods remove information from language model weights? [arXiv:2410.08827](https://arxiv.org/abs/2410.08827)
4. Dong, Z., Shen, X., & Xia, R. (2025). MEMIT-Merge: Addressing MEMIT's key-value conflicts in same-subject batch editing for LLMs. *Findings of ACL 2025*. [arXiv:2502.07322](https://arxiv.org/abs/2502.07322)
5. Duan, Z., Duan, W., Yin, Z., Shen, Y., Jing, S., Zhang, J., Shen, H., & Cheng, X. (2025). Related knowledge perturbation matters: Rethinking multiple pieces of knowledge editing in same-subject. *NAACL 2025*. [arXiv:2502.06868](https://arxiv.org/abs/2502.06868)
6. Holmov, A., Youssef, P., Schoots, N., & Seifert, C. (2026). One mask to rule them all: On hidden facts after editing and how to find them. *Findings of ACL 2026*. [arXiv:2605.28839](https://arxiv.org/abs/2605.28839)
7. Hu, C., Cao, P., Chen, Y., Liu, K., & Zhao, J. (2025). Knowledge in superposition: Unveiling the failures of lifelong knowledge editing for large language models. *AAAI 2025*. [arXiv:2408.07413](https://arxiv.org/abs/2408.07413)
8. Levine, N., Duvenaud, D., & Radford, A. (2026). Introducing talkie: a 13B vintage language model from 1930. [talkie-lm.com](https://talkie-lm.com/introducing-talkie)
9. Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and editing factual associations in GPT. *NeurIPS 2022*. [arXiv:2202.05262](https://arxiv.org/abs/2202.05262)
10. Minder, J., Dumas, C., Slocum, S., Casademunt, H., Holmes, C., West, R., & Nanda, N. (2025). Narrow finetuning leaves clearly readable traces in activation differences. [arXiv:2510.13900](https://arxiv.org/abs/2510.13900)
11. Nanda, N., Rajamanoharan, S., Kramár, J., & Shah, R. (2023). Fact finding: Attempting to reverse-engineer factual recall on the neuron level. *AI Alignment Forum*. [alignmentforum.org](https://www.alignmentforum.org/posts/iGuwZTHWb6DFY3sKB/fact-finding-attempting-to-reverse-engineer-factual-recall)
12. Nief, T., Reber, D., Richardson, S., & Holtzman, A. (2025). Dynamic weight grafting: Localizing finetuned factual knowledge in transformers. [arXiv:2506.20746](https://arxiv.org/abs/2506.20746)
13. O'Neill, C., Kirkby, M., Liu, J., & Psenka, M. (2026). Can a language model continually learn facts in its weights? *NeurIPS 2026 Workshop on Continual Learning in the Era of Foundation Models and Embodied Agents*. [arXiv:2607.11020](https://arxiv.org/abs/2607.11020)
14. Sun, C., Aksitov, R., Zhmoginov, A., Miller, N. A., Vladymyrov, M., Rueckert, U., Kim, B., & Sandler, M. (2025). How new data permeates LLM knowledge and how to dilute it. *ICLR 2025*. [arXiv:2504.09522](https://arxiv.org/abs/2504.09522)
15. Tan, D., Bostock, J., draganover, Martinez, A., sidbaines, & Africa, D. (2026). Your model organisms might be fried. *LessWrong*. [lesswrong.com](https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried)
16. Vig, J., Gehrmann, S., Belinkov, Y., Qian, S., Nevo, D., Singer, Y., & Shieber, S. (2020). Investigating gender bias in language models using causal mediation analysis. *NeurIPS 2020*. [proceedings.neurips.cc](https://proceedings.neurips.cc/paper_files/paper/2020/file/92650b2e92217715fe312e6fa7b90d82-Paper.pdf)

**(A) Sequential facts**

Facts in order, labelled as in Figure 2. The facts, training items and held-out questions are released in [basetenlabs/talkie-facts-replication](https://github.com/basetenlabs/talkie-facts-replication).

| Write | Fact | Answer (brief) | 
|---|---|---|
| 1 | 2011 UEFA Champions League final | Wembley Stadium | 
| 2 | Taylor, triple jump (2015 World Championships) | 18.21 metres | 
| 3 | 2011 UEFA Europa League final | 1–0 (Porto–Braga) | 
| 4 | 2014 Commonwealth Games | Glasgow | 
| 5 | 2015–16 Premier League | Leicester City | 
| 6 | USA, Rio 2016 | 46 gold medals | 
| 7 | Bolt, 200 m final (London 2012) | 19.32 seconds | 
| 8 | 2016 UEFA Europa League final | 3–1 (Sevilla–Liverpool) | 
| 9 | 2018 Stanley Cup | Washington Capitals | 
| 10 | 2014 UEFA Champions League final | Estádio da Luz | 
| 11 | Rio 2016 opening ceremony | 5 August 2016 | 
| 12 | 2011 Wimbledon (women's) | Kvitová | 
| 13 | NBA regular-season MVP (2014–15) | Stephen Curry | 
| 14 | 2018 Youth Olympics opening ceremony | 6 October 2018 | 
| 15 | 2019 US Open (women's) | Andreescu | 
| 16 | Japan, Rio 2016 | 12 gold medals | 
| 17 | NBA regular-season MVP (2017–18) | James Harden | 
| 18 | NBA regular-season MVP (2013–14) | Kevin Durant | 
| 19 | 2013 IAAF World Championships | Moscow | 
| 20 | Suhr, indoor pole vault (2013) | 5.02 metres | 

**(B) Grading**

We graded with an LLM judge (GPT-5-mini, with GPT-5 re-checking difficult cases).

**(C) Patching and update removal**

For each of 120 randomly sampled loss events, we ran the post-fact model on the earlier fact's question and replaced the output of one component type (MLP or attention) in one block of layers with its value from the pre-write model, reporting the fraction of the lost true-answer log-probability that was restored:

$$
\text{restored} = \frac{\log p_{\text{intervened}}(a) - \log p_{\text{after}}(a)}{\log p_{\text{before}}(a) - \log p_{\text{after}}(a)}
$$

where "before" and "after" are the models either side of the competing fact write, and *a* is the correct answer. For update removal, we subtracted the newer fact's merged update from the same blocks. Layers are numbered 1–40. Bars show medians across events, with bootstrap 95% confidence intervals.
