---
title: How UK AISI and EvalEval Are Making Benchmark Results Reproducible
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: huggingface
url: https://huggingface.co/blog/evaleval-aisi
author: Avijit Ghosh; Jenny Chim; Deep Joshi; Srishti; Matt Kennedy; Irene Solaiman;
  Jessica McFadyen; Lynn Tan; Coz
published: '2026-09-22'
fetched: '2026-09-23T06:18:38Z'
classifier: null
taxonomy_rev: 2
words: 806
content_sha256: 7d82baab98e355f6700907ef5560aae8941613d8d7fe0d386f16e9bb74425528
---

# How UK AISI and EvalEval Are Making Benchmark Results Reproducible

# 
	
		
	
	
		How UK AISI and EvalEval Are Making Benchmark Results Reproducible
	

 [Update on GitHub](https://github.com/huggingface/blog/blob/main/evaleval-aisi.md)

  [Upvote 8](https://huggingface.co/login?next=%2Fblog%2Fevaleval-aisi) 

![Avijit Ghosh's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/k8UMg_tnorG_uCXidybZ7.jpeg) 

[Avijit Ghoshevijit](https://huggingface.co/evijit)    

![EvalEval Coalition's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/DIq15x1lEAs67aD3qLFuV.png)

[evaleval](https://huggingface.co/evaleval)

[Jenny Chimj-chim](https://huggingface.co/j-chim)    

![EvalEval Coalition's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/DIq15x1lEAs67aD3qLFuV.png)

[evaleval](https://huggingface.co/evaleval)

![Deep Joshi's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/682434234254a325ecf16a29/PBoBR5WX9PA7IZqjcMOS8.png) 

[Deep Joshideeplumiere](https://huggingface.co/deeplumiere)    

![EvalEval Coalition's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/DIq15x1lEAs67aD3qLFuV.png)

[evaleval](https://huggingface.co/evaleval)

[Srishtisrishtiy](https://huggingface.co/srishtiy)    

![EvalEval Coalition's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/DIq15x1lEAs67aD3qLFuV.png)

[evaleval](https://huggingface.co/evaleval)

[Matt Kennedywmmkennedy](https://huggingface.co/wmmkennedy)    

![EvalEval Coalition's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/DIq15x1lEAs67aD3qLFuV.png)

[evaleval](https://huggingface.co/evaleval)

![Irene Solaiman's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/62543749b777cd32720675c2/EF_KRZO4hTo8TWXOtvc-n.png) 

[Irene Solaimanirenesolaiman](https://huggingface.co/irenesolaiman)    

![EvalEval Coalition's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/6413251362e6057cbb6259bd/DIq15x1lEAs67aD3qLFuV.png)

[evaleval](https://huggingface.co/evaleval)

[Jessica McFadyenmcfadyen-aisi](https://huggingface.co/mcfadyen-aisi)    

![UK AI Security Institute's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/XIeCCLH_sP7yKBAjkg9N1.png)

[ai-safety-institute](https://huggingface.co/ai-safety-institute)

[Lynn Tanlynn-aisi](https://huggingface.co/lynn-aisi)    

![UK AI Security Institute's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/XIeCCLH_sP7yKBAjkg9N1.png)

[ai-safety-institute](https://huggingface.co/ai-safety-institute)

[Cozcoz-aisi](https://huggingface.co/coz-aisi)    

![UK AI Security Institute's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/noauth/XIeCCLH_sP7yKBAjkg9N1.png)

[ai-safety-institute](https://huggingface.co/ai-safety-institute)

[EvalEval Coalition](https://evalevalai.com/)is thrilled to share that the

[UK AI Security Institute (AISI)](https://www.aisi.gov.uk/)is using EvalEval's infrastructure to openly share evaluation results, supporting more reproducible and verifiable evaluation science.

AISI and EvalEval have previously collaborated on research that began at a [joint workshop alongside NeurIPS 2025](https://evalevalai.com/events/workshop-2025/), and feedback from the Institute has helped shape the [Every Eval Ever (EEE) schema](https://evalevalai.com/projects/every-eval-ever/). This next phase of the collaboration puts that shared infrastructure into practice.

## 
	
		
	
	
		Why reproducible evaluation reporting matters
	

As AI deployment accelerates, evaluations are becoming increasingly important sources of evidence about model and system performance. Yet results are reported across many formats, platforms, and outlets, often without enough information to reproduce them. Running the evaluations again may itself be prohibitively expensive.

EvalEval's mission is to improve this ecosystem through a shared reporting schema, [Every Eval Ever](https://evalevalai.com/projects/every-eval-ever/), and an open platform, [Evaluation Cards](https://evalcards.evalevalai.com/), that brings evaluation results and the information needed to interpret them into a common structure.

This builds naturally on AISI's work to make evaluation more efficient through [OptStop](https://arxiv.org/abs/2608.14425), more statistically rigorous through [HiBayES](https://www.aisi.gov.uk/blog/hibayes-improving-llm-evaluation-with-hierarchical-bayesian-modelling), and more standardised in areas including transcript analysis and capability elicitation. Together, AISI and EvalEval are working to diagnose gaps in evaluation reporting and build shared infrastructure to close them.

## 
	
		
	
	
		What AISI is sharing
	

Transcript-level transparency matters not only for reproducibility, but also for analysis and diagnosis. In this new phase of the collaboration, AISI is making publicly reported evaluation methods and findings available through Evaluation Cards where appropriate. The release includes verified results, context, and configuration information for the five benchmarks in the paper's main experiment:

- HealthBench
- FrontierMath
- Humanity's Last Exam
- SWE-Bench Pro
- Terminal-Bench 2.0

These results cover six frontier models: Claude Opus 4, Claude Opus 4.5, Claude Opus 4.6, GPT-5, GPT-5.2, and GPT-5.4. The release also includes results from two related cyber evaluations—Cyber CTFs and The Last Ones—which use a different, partially overlapping set of models. The data accompany AISI's paper, [*How Inference Compute Shapes Frontier LLM Evaluation*](https://arxiv.org/abs/2606.17930), which studies how benchmark performance depends on inference-time compute and evaluation protocol.

*Performance on Humanity's Last Exam changes with evaluation protocol and inference compute. Each curve shows the cumulative share of attempted tasks solved within a given token count, using the earliest observed success per task. When models received correctness feedback from an oracle after each attempt, they continued to solve additional tasks as token use increased.*

When results are openly released with setup information, researchers and practitioners can examine individual studies more closely and compare findings across the wider ecosystem. Where other reports lack these details, releases like AISI's provide verified reference points for interpreting evaluations in context—for example, by helping researchers understand how setup choices may influence reported performance. As more evaluators adopt EEE, open comparisons like these can support broader and more reliable meta-research.

*AISI's Terminal-Bench 2.0 results alongside other reported evaluations for the same models, under different evaluation setups.*

We are excited about this adoption and look forward to further standardising and sharing evaluations with AISI and other AI evaluation organisations.

## 
	
		
	
	
		Contribute to the shared mission
	

- **Model developers:**[Report verified evaluation results](https://evalcards.evalevalai.com/help/get-verified) .
- **Evaluation developers:** Report benchmarks and run data using the[Every Eval Ever schema](https://github.com/evaleval/every_eval_ever) .
- **Evaluation, governance, and policy researchers:**[Explore Evaluation Cards](https://evalcards.evalevalai.com/) by benchmark or model, or use it to examine the state of evaluation reporting as a whole.

## 
	
		
	
	
		About the EvalEval Coalition
	

The EvalEval Coalition is a research community developing scientifically grounded research and robust deployment infrastructure for the evaluation ecosystem. Its goal is to improve evaluation science, address the lack of consensus around documenting evaluation applicability and utility, and broaden coverage of the impacts that matter for scientific research and policy analysis.

The coalition's flagship projects include [Every Eval Ever](https://evalevalai.com/projects/every-eval-ever/), a shared schema and repository for evaluation results, and [Evaluation Cards](https://evalevalai.com/projects/eval-cards/), which combines benchmark metadata, evaluation-run data, and model metadata into interpretable records. Together, they make it easier to understand when apparently similar scores were produced under meaningfully different conditions.

## 
	
		
	
	
		About the UK AI Security Institute
	

The [UK AI Security Institute](https://www.aisi.gov.uk/) is a research organisation within the UK government's Department for Science, Innovation and Technology. Its mission is to equip governments with a scientific understanding of the risks posed by advanced AI. AISI conducts research and builds infrastructure to understand advanced AI capabilities and impacts, develop and test mitigations, and inform policy.
