---
title: Feature flags for production AI
kind: blog
topic: infra-platform
subtopic: deployment
secondary_topics:
- evals-observability/evaluation
summary: Shows how to use Pydantic Logfire's typed managed variables as feature flags
  for production AI systems, letting teams target and A/B test models, prompts, and
  tool policies (with UsageLimits caps) without redeploying, and tying each resolved
  variant to OpenTelemetry traces and dashboards.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/feature-flags-for-production-ai
author: Jameson Lee
published: '2026-08-18'
fetched: '2026-08-19T06:14:02Z'
classifier: claude
taxonomy_rev: 2
words: 1567
content_sha256: df3b0e65e4c86a0ae38ecb1c4befc36964515dd4daf70d103f2d7bcff861b106
---

# Feature flags for production AI

AI makes software accessible to more people. One agent may serve an AI-native specialist and a first-time user who expects an ordinary request to work. It may support several languages, levels of domain expertise, and workflows that combine model responses with tools and application logic.

A single default experience will rarely suit everyone. [Pydantic Logfire managed variables](https://pydantic.dev/docs/logfire/manage/managed-variables/) give AI engineers a control plane for changing the three primitives that shape an AI application: models, prompts, and tools. Here, feature flags are not limited to booleans. They are typed, versioned variables that teams can target, measure, and change without redeploying.

The foundation of A/B testing still applies: define alternatives, assign traffic, and compare outcomes. Generative AI expands what we can test and what we need to measure. Teams must find the right experience while balancing quality, cost, latency, and reliability.

## 

Growth engineering is now part of AI engineering. AI engineers run product experiments while building backends, frontends, and the analytics needed to understand how their work performs.

The result is more complex than a click or conversion. A production AI experiment should consider:

- Answer quality and task completion
- Cost per successful outcome
- Latency and time to first useful response
- Tool accuracy and retry behavior
- Safety, reliability, and escalation
- Performance across languages, cohorts, and levels of expertise

The questions are simple, even when the answers are not. Does it work? For whom? Under what conditions? How quickly? At what cost? Does it use the right tools, and can it fail safely?

Shipping faster can produce a better product as providers release models, frameworks add capabilities, and useful patterns emerge. A shorter feedback loop gives teams more chances to learn before the technology moves again.

## 

AI teams can start with three things.

Install the managed variables extra before using these examples:

```
pip install 'logfire[variables]'
```
1. 
**Models** determine capabilities, speed, cost, context limits, and provider behavior. A string variable can route an opted-in group to a new model without changing application code:```
import logfire
logfire.configure()
logfire.instrument_pydantic_ai()
model = logfire.var(
    name='support_model',
    type=str,
    default='openai:gpt-5.2',
)
```
2. 
**Prompts** frame the task, provide domain guidance, and shape how the application communicates. A managed prompt can compare a guided experience with a concise one:```
instructions = logfire.var(
    name='support_instructions',
    type=str,
    default='Explain the next step clearly and ask before taking action.',
)
```
3. 
**Tools** determine what the system can retrieve, calculate, or change. The variable should contain a typed policy, not executable code:```
from typing import Literal
from pydantic import BaseModel, Field
class ToolPolicy(BaseModel):
    profile: Literal['answer_only', 'research', 'diagnostic']
    max_tool_calls: int = Field(ge=0, le=8)
tool_policy = logfire.var(
    name='tool_policy',
    type=ToolPolicy,
    default=ToolPolicy(
        profile='answer_only',
        max_tool_calls=3,
    ),
)
```
The application maps each profile to pre-approved tools and enforces the call limit. Tool code, credentials, authorization, and required approvals stay in code.

These primitives affect one another. A better prompt may make a smaller model viable. A stronger model may need fewer examples but call an expensive tool too often. Teams should test them together and connect each combination to product and operational results.

## 

Defining variables is only the start. The application must resolve and apply them during an agent run.

This example uses the user ID as a stable targeting key. It also supplies the tenant plan and workflow for conditional routing. The resolved tool policy becomes a limit that [Pydantic AI](https://pydantic.dev/docs/ai/overview/) enforces:

```
from pydantic_ai import Agent, UsageLimits
APPROVED_TOOLS = {
    'answer_only': [],
    'research': [support_search],
    'diagnostic': [support_search, account_diagnostics],
}
async def answer(user_id: str, tenant_plan: str, message: str) -> str:
    attributes = {
        'tenant_plan': tenant_plan,
        'workflow': 'customer_support',
    }
    with (
        model.get(targeting_key=user_id, attributes=attributes) as selected_model,
        instructions.get(targeting_key=user_id, attributes=attributes) as selected_instructions,
        tool_policy.get(targeting_key=user_id, attributes=attributes) as selected_policy,
    ):
        policy = selected_policy.value
        agent = Agent(
            selected_model.value,
            instructions=selected_instructions.value,
            tools=APPROVED_TOOLS[policy.profile],
        )
        result = await agent.run(
            message,
            usage_limits=UsageLimits(tool_calls_limit=policy.max_tool_calls),
        )
        return result.output
```
A high-volume support workflow might receive one research call. An approved diagnostic workflow might receive four. `UsageLimits` checks the cap before it executes more tools, protecting cost and latency from a runaway loop.

The variable contexts also add the selected labels and versions to downstream spans. Engineers can see which model, prompt, and tool policy produced each result.

## 

The emphasis on **typed** matters. Pydantic began by helping developers turn untrusted data into validated objects. Managed variables bring the same idea to production configuration: [Logfire](https://pydantic.dev/logfire) can change a value, but the application still declares its valid shape.

Variables can hold:

- **Text** for prompts, instructions, and messages
- **Numbers** for token limits, thresholds, and budgets
- **Booleans** for on-or-off flags
- **Structured data** for dataclasses and Pydantic models
- **Templates** that combine runtime inputs with reusable fragments

The code default acts as a contract and a safety net. Logfire validates remote values against the declared type or JSON Schema. If a value is missing or invalid, the application uses its known-good default. Teams can change one primitive at a time or group a model, prompt, and tool policy in one Pydantic model so the whole experience changes together.

## 

Versions can receive labels such as `production`, `canary`, `control`, and `treatment`. Percentage routing controls how much traffic receives each label. A stable `targeting_key`, such as a user or tenant ID, keeps the assignment consistent across requests.

Sampling is only one option. [Conditional targeting rules](https://pydantic.dev/docs/logfire/manage/managed-variables/targeting/) can select an experience using explicit resolution attributes, OpenTelemetry resource attributes, or request baggage. Useful attributes include language, plan, region, workflow, service version, and beta enrollment. Logfire checks rules in order and uses the first match.

This gives engineers more control than sending 10% of all traffic to a treatment. A team might offer a guided French prompt only to opted-in users during onboarding. During a capacity incident, it might route one tenant plan to a cheaper model. Each resolution creates a span, and the chosen label and version flow into the work that follows.

## 

After defining the variables, push their metadata and generated schemas to Logfire:

```
if __name__ == '__main__':
    logfire.variables_push()
```
This command requires a `LOGFIRE_API_KEY` with the `project:write_variables` scope. The runtime application uses the separate `project:read_variables` scope.

The rest of the lifecycle lives in Logfire. Teams create immutable versions, move labels, and change rollout percentages or targeting rules. To roll back, point a label at the last known-good version. No application deploy is required.

## 

Feature flags determine which experience runs. Observability shows what happened next. Logfire connects variable versions to traces and [SQL-backed dashboards](https://pydantic.dev/docs/logfire/observe/dashboards/), so product and system results share the same OpenTelemetry context.

Two dashboards make a useful start:

1. **Product results:** task completion, abandonment, repeat use, escalation, and feedback, grouped by variable label, version, and cohort.
2. **System results:** latency, tokens, inference cost, tool calls, retries, and errors for the same groups.

The first shows whether the experience helped. The second shows what it cost. Alerts can identify a sustained problem and link an engineer to the relevant traces and configuration.

Together, these parts form a continuous evidence loop. Production traces reveal failures worth investigating. Teams preserve those cases, assess a proposed change, and use feature flags to return a new model, prompt, or tool configuration to production.

![Continuous improvement loop connecting production traces, failures, datasets, evaluations, and feature flags.](https://pydantic.dev/assets/blog/feature-flags-for-production-ai/continuous-evidence-loop.png)


## 

### 

A customer asking for help with an unfamiliar task may need translated instructions, guided steps, or a direct answer. Teams can compare prompts written for each language, route ambiguous requests to a stronger model, and vary tool access. Completion, clarification turns, escalation, latency, and cost show whether the added guidance helps.

### 

One user may know the specialist terms and want the source immediately. Another needs acronyms and assumptions explained. Teams can target configurations by organization, role, or selected expertise. They can vary domain instructions, retrieval sources, citation requirements, response depth, and analytical tools. Task completion, follow-up questions, and corrections from subject-matter experts point to the next experiment.

### 

An agent embedded in a SaaS product may investigate problems across tenants. One tenant might generate large contexts, repeated tool calls, and high inference costs. Teams can test model routes, context limits, summarization prompts, and tool policies for that tenant before changing the experience for everyone.

Logfire traces connect tenant context with tokens, cost, latency, retries, and results. A SQL alert can detect sustained abnormal usage. An event-triggered judge can then produce a trace-linked explanation for an engineer instead of returning only an `expensive` label.

## 

Feature flags belong inside the AI engineering and observability workflow. This keeps the change, the targeting decision, and the result connected. Engineers can release an experience to the right group, observe its product and system effects, notify the right people, and roll it back without losing attribution.

The boundary remains important. Code governs schemas, business logic, permissions, and safety rules. Managed variables govern the parts of models, prompts, and tool policies that should change at runtime. OpenTelemetry connects each decision to what follows.

This control plane can support more complex workflows. A model variable can select a [Logfire AI Gateway](https://pydantic.dev/docs/logfire/manage/ai-gateway/) routing group with provider failover and load balancing. Targeting can use OpenTelemetry attributes from real production traffic. An internal application can add roster or group membership as routing context.

A feature flag never grants authorization. Code still decides what a user or agent may do. Managed variables make the behavior that should change visible, versioned, and reversible. They give AI engineers, and authorized agents working with them, the context needed to investigate results and improve production systems safely.
