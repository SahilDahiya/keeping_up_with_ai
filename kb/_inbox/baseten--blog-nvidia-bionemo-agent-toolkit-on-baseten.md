---
title: NVIDIA BioNeMo Agent Toolkit on Baseten
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: baseten
url: https://www.baseten.co/blog/nvidia-bionemo-agent-toolkit-on-baseten
author: Fred Liu
published: '2026-06-23'
fetched: '2026-11-12T06:15:02Z'
classifier: null
taxonomy_rev: 2
words: 1459
content_sha256: fcdb5ff73e9b00524fc9e89f74d18a80b852b0a03569640dc459febdafebb243
---

# NVIDIA BioNeMo Agent Toolkit on Baseten

AI models
# NVIDIA BioNeMo Agent Toolkit on Baseten

Empowering AI agents to accelerate scientific discovery


- Authors
- Date
- June 23, 2026

TLDR

NVIDIA BioNeMo Agent Toolkit helps transform general-purpose AI agents into scientific agents capable of performing real biological and drug discovery tasks. The toolkit combines BioNeMo Skills, open models, NVIDIA NIM microservices, and agent infrastructure to enable workflows such as protein structure prediction, protein design, virtual screening, genomics analysis, and target discovery. All BioNeMo NIM microservices are available today in the Baseten Model Library, making it easy for developers to deploy and scale scientific AI applications.

Scientific AI is evolving from isolated model inference toward agentic workflows that can reason, plan, and execute across multi-step scientific tasks. Scientists increasingly need AI systems that can understand scientific literature, predict protein structures, design molecules, analyze genomic data, identify therapeutic targets, and recommend next experiments

NVIDIA BioNeMo Agent Toolkit provides the domain-specific tools, models, and skills needed to enable this new generation of AI scientists. It combines BioNeMo skills, open models, NVIDIA NIM microservices, and agent orchestration infrastructure, to help agents move from reading science to doing science.

At Baseten, we built our platform for teams that need to run inference at scale and increasingly, those teams are in life sciences. The shift toward agentic workflows is changing what 'running a model' means: instead of a single call, an agent is now orchestrating a pipeline of specialized models, each passing structured outputs to the next. That's exactly the infrastructure problem Baseten was built to solve. So when NVIDIA shared the BioNeMo agent toolkit with us, it gave us the biological reasoning layer our customers were missing. BioNeMo NIM are domain-specific by design — not general-purpose models adapted for biology, but models trained from the ground up for structure prediction, molecule generation, and genomics. Pairing that with Baseten's inference infrastructure means a life science research team can run a full discovery pipeline end-to-end, without standing up and managing the underlying compute themselves

NVIDIA NIM microservice is a Docker container that serves exactly one model behind a small HTTP API, with the weights, CUDA, and the serving stack baked in. [BioNeMo](https://github.com/NVIDIA-BioNeMo) is an NVIDIA platform for AI-driven biology and drug discovery, providing open models, libraries, datasets, tools, and NIM microservices for scientific AI workloads. The BioNeMo portfolio spans three broad categories:

1. **Understanding Biology** - models that analyze biological sequences and identify biological meaning,  such as mapping a molecule’s 3D shape from its raw sequence. Examples include [Evo 2](https://build.nvidia.com/nvidia/evo2-protein-design)
2. **Design New Therapeutics** - models that generate proteins, antibodies, and molecules, such as designing entirely new, functional proteinsto target specific diseases. Examples include [RFdiffusion,](https://build.nvidia.com/ipd/rfdiffusion) [ProteinMPNN,](https://build.nvidia.com/ipd/proteinmpnn) [GenMol](https://build.nvidia.com/nvidia/genmol-generate), [MolMIM](https://build.nvidia.com/nvidia/molmim-generate).

The table below summarizes the BioNeMo NIM microservices [available on Baseten](https://www.baseten.co/library/):

| NIM | What it does | Inputs → outputs | 
|---|---|---|
| OpenFold2 | Single-chain structure prediction, AlphaFold2-style | Sequence plus an alignment → a PDB or mmCIF structure, plus confidence score | 
| OpenFold3 | Diffusion structure prediction for complexes of protein, DNA, RNA, and small molecules | Sequences or molecule strings → a structure plus pLDDT, pTM, and ipTM scores | 
| Boltz2 | Structure prediction with optional binding-affinity prediction for a ligand | Polymers plus an optional ligand →a structure, a predicted pIC50, and a probability that it binds | 
| RFdiffusion | De novo protein backbone design, including binders to a target | A contig spec plus an optional template → a designed backbone (PDB) | 
| ProteinMPNN | Inverse folding: invent a sequence that will fold into a given backbone | A backbone (PDB) → candidate sequences plus scores | 
| GenMol | Molecule generation and scaffold decoration in SAFE notation | A masked molecule string → new molecules (SMILES) plus a property score | 
| MolMIM | Latent-space molecule generation, embedding, and property optimization | A seed molecule → optimized molecules plus scores | 
| DiffDock | Blind protein-ligand docking by diffusion | Protein structure plus a ligand → ranked binding poses plus confidence | 
| MSA-Search | GPU MMseqs2 search for a protein's evolutionary relatives (the ColabFold step) | Amino acid sequence → a multiple sequence alignment (A3M text) | 
| Evo2 7B Evo2 40B | Genomic foundation model (7B and 40B): DNA generation and layer embeddings | A DNA sequence → generated DNA or per-token features | 

Alongside the containers, NVIDIA is publishing BioNeMo skills. A skill is a markdown specification written for an agent. It gives instructions on which endpoint to call for a given task, the authentication header, the exact payload fields, how to parse the response, and what the common errors mean. Each model gets one SKILL.md plus reference files, and two "meta-skills" compose several models into full pipelines.

When you point an agent at these skills, it can decide on its own that folding a sequence means gathering an alignment first and folding second, format both payloads correctly, and then carry the data from one model to the next.

So the skill will turn a pile of HTTP endpoints into something an agent can drive end to end and deliver a complete scientific workflow.

Context is necessary before the structure models can run; the accuracy of AlphaFold-class models does not come from the sequence alone, it comes from evolution. Find hundreds of related proteins across other species and line them up, and the columns that mutate together over millions of years are usually touching in 3D. That coevolution signal in the alignment is most of what the folder reads, which is why folding a single lonely sequence yields noticeably worse results.

Gathering context is the whole job of MSA-Search (MSA stands for “multiple sequence alignment”): GPU MMseqs2 searches over a roughly 1.4 TB reference database, which turns a search that took tens of minutes to hours on CPU into one that finishes in seconds. It is plumbing, but the fold depends on it, so it is the first step in every pipeline outlined below.

Here is the structure named at the beginning of this blog, drawn as the agent sees it. The agent reads the meta-skill, then makes two calls, and the alignment text that comes out of the search is what the folder uses as input.

The agent picks paired search instead of standard search when the input is a complex of two chains. It can run OpenFold3 twice, once with the full alignment and once with a single-sequence alignment. Then it reads the confidence score and decides whether to trust the answer. That decision-making is what the BioNeMo skill enables.

Protein folding is only one example. BioNeMo Agent Toolkit enables broader scientific workflows, including:

- **Protein Binder Design** - design proteins that bind to specific biological targets and computationally validate their effectiveness before laboratory testing.
- **Virtual Screening** - generate, dock, score, and rank candidate drug molecules from millions of possibilities before expensive experimental validation.
- **Genomic Analysis** - combine genomics, biological foundational models, and agentic reasoning to identify and prioritize promising therapeutic targets.
- **Target Discovery** - combine genomics, biological foundation models, and agentic reasoning to identify and prioritize promising therapeutic targets.

These workflows transform isolated model calls into complete scientific discovery pipelines.

As we now want to discover new drugs, here is how the models can be used:

1. **GenMol** generates candidate molecules from a scaffold.
2. **DiffDock** aligns each candidate to the target protein and keeps only those that fit.
3. **Boltz2** then predicts how tightly each survivor would actually bind.

To finish, the agent will generate, dock, score, sort, and hand back a shortlist ranked by predicted potency. It is the same move as folding, three models instead of two, and the chemistry-design models are doing the work that the folders cannot.

All BioNeMo NIM microservices are available today in the [Baseten Model Library](https://www.baseten.co/library/family/bionemo/).

Developers can deploy them directly through Baseten's MCP and invoke them using [Baseten skills](https://github.com/basetenlabs/baseten-skills). Then, the same pattern that folds a protein or ranks drug candidates will work end-to-end: the agent reads the skill, picks the right NIM from the library, deploys it, and starts calling.

By making BioNeMo Agent Toolkit available on Baseten, developers can rapidly deploy and scale scientific AI workloads without managing the complexity of model serving, GPU infrastructure, or orchestration.

Teams like Benchling are already using Baseten to run BioNeMo workloads in production, accelerating the path from sequence to structure to candidate.

Whether you’re building protein design tools, virtual screening pipelines, genomic analysis applications, or next-generation AI scientists, Baseten provides a production-ready platform for BioNeMo-powered workloads.

Explore BioNeMo models in the [Baseten Model Library](https://www.baseten.co/library/family/bionemo/) and start building AI agents for protein design, virtual screening, genomics, and drug discovery today.

If you are building scientific AI applications and need help scaling them, [talk to our engineers](https://www.baseten.co/talk-to-us/).
