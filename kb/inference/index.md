# inference

4 articles.

- **2026-06-30** — [Using OSS models to save on inference costs without cutting quality](<serving/Using OSS models to save on inference costs without cutting quality.md>) · `serving` · braintrust
  Explains using open-source models to reduce inference cost without sacrificing quality, emphasizing eval-driven model selection and serving tradeoffs.
- **2025-09-17** — [A postmortem of three recent issues](<serving/A postmortem of three recent issues.md>) · `serving` · anthropic-engineering
  Postmortem of three overlapping serving-stack bugs that silently degraded Claude's output quality, and the detection and rollout changes made in response.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.

## Also relevant (filed elsewhere)

- **2026-07-01** — [Model subsidies are ending. What do you do now?](<../infra-platform/cost/Model subsidies are ending. What do you do now.md>) · `cost` · arize
  Analyzes the end of subsidized LLM pricing and what agentic task success rates imply for real inference cost per correct result.
- **2026-06-15** — [Growing the Cloudflare AI team with talent from Ensemble AI](<../industry/announcements/Growing the Cloudflare AI team with talent from Ensemble AI.md>) · `announcements` · cloudflare-ai
  Ensemble AI's team joins Cloudflare's Workers AI to improve inference economics, bringing NdLinear — a drop-in linear-layer replacement operating on multidimensional activations to cut parameters and compute — and NdLinear-LoRA for parameter-efficient fine-tuning, complementing Infire and Unweight.
- **2026-03-16** — [Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider](<../infra-platform/deployment/Arize AX Adds Native Support for NVIDIA NIM as AI Model Provider.md>) · `deployment` · arize
  Announces native NVIDIA NIM support in Arize AX so teams can connect hosted model providers into evaluation and observability workflows.
- **2025-08-13** — [Evaluating Model Performance Across Clouds](<../models/benchmarks/Evaluating Model Performance Across Clouds.md>) · `benchmarks` · langfuse
  Evaluates model performance across cloud providers, focusing on latency, cost, quality, and provider-selection tradeoffs for production inference.
- **2025-06-05** — [Accurate KV Cache Quantization with Outlier Tokens Tracing](<quantization/Accurate KV Cache Quantization with Outlier Tokens Tracing.md>) · `quantization` · arize
  Summarizes research on KV-cache quantization with outlier token tracing to reduce LLM inference memory cost while preserving output quality.
- **2024-01-16** — [Generation configurations: temperature, top-k, top-p, and test time compute](<../models/reasoning/Generation configurations temperature, top-k, top-p, and test time compute.md>) · `reasoning` · chip-huyen
  Explains decoding parameters such as temperature, top-k, top-p, and test-time compute, connecting generation configuration to reliability, diversity, latency, and cost.
- **2023-09-19** — [Arize AI Debuts Integration with Anyscale Endpoints](<../infra-platform/deployment/Arize AI Debuts Integration with Anyscale Endpoints.md>) · `deployment` · arize
  Announcement and integration walkthrough for using Arize with Anyscale Endpoints to monitor hosted open-model inference.
- **2021-09-07** — [A friendly introduction to machine learning compilers and optimizers](<optimization/A friendly introduction to machine learning compilers and optimizers.md>) · `optimization` · chip-huyen
  Introduces machine-learning compilers and optimizers, explaining graph-level and operator-level optimizations, hardware targets, and why compiler stacks matter for model speed and deployment.
