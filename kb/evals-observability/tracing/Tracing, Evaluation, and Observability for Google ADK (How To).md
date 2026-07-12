---
title: Tracing, Evaluation, and Observability for Google ADK (How To)
topic: evals-observability
subtopic: tracing
secondary_topics:
- agents/planning
summary: How-to guide for tracing, evaluating, and observing Google ADK agents in
  production-style workflows.
source: arize
url: https://arize.com/blog/tracing-evaluation-and-observability-for-google-adk-how-to/
author: Richard Young
published: '2025-11-14'
fetched: '2026-07-11T04:54:00Z'
classifier: codex
taxonomy_rev: 1
words: 1730
content_sha256: d97fc77001dd9fe8d97312b6edb62f7903d0c3ab27e43290b93aaa646f3f0b7a
---

# Tracing, Evaluation, and Observability for Google ADK (How To)

Multi-agent systems are moving from research prototypes to production deployments. But there’s a gap between “it works in the demo” and “it works reliably at scale.” [Google’s Agent Development Kit (ADK)](https://google.github.io/adk-docs/) handles the orchestration complexity, while [Arize AX](https://arize.com/generative-ai/) can provide the observability needed to understand and optimize agent behavior in production.

This post walks through building a real travel concierge system that demonstrates both frameworks working together. You’ll see how ADK’s modular architecture enables complex agent coordination while the Arize AX platform provides visibility into every decision, tool call, and handoff.

## Evaluation and Observability 🤝 Google ADK

### ADK: Redefining Agent Development

ADK’s strength lies in its code-first, modular approach to multi-agent orchestration. Rather than forcing rigid patterns, it offers Python flexibility with built-in support for state management, callbacks, and streaming. Model-agnostic yet optimized for Gemini and Google Cloud’s Vertex AI platform, ADK provides a seamless path from development to enterprise deployment.

The framework excels in three areas:

- *Multi-Agent Architecture*: Build scalable applications by composing specialized agents into flexible hierarchies. ADK supports both deterministic workflows and adaptive, LLM-driven routing.
- *Rich Tool Ecosystem*: Integrate pre-built tools for search, code execution, or MCP; extend with LangChain, LlamaIndex, or even other agents as tools—enabling interaction with virtually any external system.
- *Production-Ready Infrastructure*: With containerization, deployment hooks for Google Cloud, and evaluation-ready developer tooling (CLI and web interfaces), ADK shortens the path from prototype to production.

### Arize AX: Agent Observability Platform

While ADK powers development, Arize AX brings clarity and control to production. Trusted at a trillion-inference scale, Arize AX delivers observability and evaluation purpose-built for complex agent systems. The Arize AX platform addresses the unique challenges of agent systems through several key capabilities:

- *Comprehensive Evaluation*: Assess decision pathways, tool-use efficiency, and coordination quality to pinpoint where agents succeed or struggle.
- *Development-to-Production Continuity*: Enable evaluation-driven workflows where- [LLM-as-a-Judge assessments](https://arize.com/llm-as-a-judge/)and production feedback loops fuel continuous improvement.
- *Prompt Optimization*: Compare, iterate, and- [A/B test prompts](https://arize.com/resource/ab-testing-for-llm-applications/)in the Prompt Playground to refine agent behavior at scale.
 Real-Time Observability: Using OpenTelemetry, Arize AX captures every decision and interaction, giving developers full visibility into non-deterministic behavior.

### Integration Advantage

Together, ADK and AX deliver a unified experience for building, deploying, and refining agent systems. ADK orchestrates; AX observes and optimizes. Through shared OpenTelemetry standards, ADK agents send telemetry directly to Arize AX without vendor lock-in — providing flexibility, insight, and confidence from prototype to production.

## The Travel Concierge Architecture

Our example system uses six specialized agents coordinated by a root orchestrator. Each agent handles a specific phase of the travel journey:

- *Inspiration Agent*– Suggests destinations and activities
- *Planning Agent*– Manages flight search, seat selection, hotel booking, and itinerary creation
- *Booking Agent*– Processes payments and confirmations
- *Pre-Trip Agent*– Gathers visa, medical, and travel advisory information
- *In-Trip Agent*– Provides real-time transit assistance and local guidance
- *Post-Trip Agent*– Captures feedback and user preferences

The root agent analyzes requests and delegates to specialists based on context. If you ask about flights, it routes to the planning agent. Questions about current location route to the in-trip agent.

## Code Walkthrough: Setting up ADK Multi-Agent Orchestration + Arize AX Evals, Tracing, and Observability

To run this example you will need the following prerequisites:

- Google Cloud Project with billing enabled
- Vertex AI API enabled
- Arize AX account ([free tier available](https://app.arize.com/auth/join))
- Python 3.11+ with Poetry

### Multi-Agent Architecture

The ADK root agent coordinates all sub-agents and determines routing logic:

```
```
```
root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A Travel Concierge using multiple sub-agents",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        inspiration_agent,
        planning_agent,
        booking_agent,
        pre_trip_agent,
        in_trip_agent,
        post_trip_agent,
    ],
    before_agent_callback=_load_precreated_itinerary,
)
```
			The system prompt guides routing decisions:

```
```
ROOT_AGENT_INSTR = """
You are an exclusive travel concierge agent helping users discover, plan, and book vacations.
....
Trip phases logic:
- If current date is before trip start_date → delegate to pre_trip agent
- If current date is between start and end dates → delegate to in_trip agent
- If current date is after end_date → delegate to post_trip agent
For planning questions (flights, hotels, seats) → transfer to planning_agent
For booking and payments → transfer to booking_agent
For inspiration and activities → transfer to inspiration_agent
"""

			#### Access to Specialized Tools

Agents use tools to interact with external systems. Here’s the Google Search grounding tool:

```
```
```
_search_agent = Agent(
    model="gemini-2.5-flash",
    name="google_search_grounding",
    description="Provides Google-search grounding capability",
    instruction="""
    Answer questions directly using google_search grounding tool.
    Provide brief, actionable information for travelers.
    Focus on immediate next steps rather than asking users to look things up.
    """,
    tools=[google_search],
)
google_search_grounding = AgentTool(agent=_search_agent)
```
			#### Memory Management with Session State

ADK uses session state for memory. In production, this should connect to external databases or Google’s Vertex AI Memory Bank:

```
```
```
def memorize(key: str, value: str, tool_context: ToolContext):
    """Store key-value pairs in session state"""
    mem_dict = tool_context.state
    mem_dict[key] = value
    return {"status": f'Stored "{key}": "{value}"'}
def memorize_list(key: str, value: str, tool_context: ToolContext):
    """Append values to lists in session state"""
    mem_dict = tool_context.state
    if key not in mem_dict:
        mem_dict[key] = []
    if value not in mem_dict[key]:
        mem_dict[key].append(value)
    return {"status": f'Stored "{key}": "{value}"'}
```
			### Integrating Observability

Adding observability takes just a few lines:

```
```
```
import os
from arize.otel import register
from openinference.instrumentation.google_adk import GoogleADKInstrumentor
tracer_provider = register(
    space_id = os.getenv("ARIZE_SPACE_ID"),
    api_key = os.getenv("ARIZE_API_KEY"),
    project_name = "adk-travel-concierge",
)
GoogleADKInstrumentor().instrument(tracer_provider=tracer_provider)
```
			Every agent decision, tool call, and handoff now flows to Arize AX as structured trace data.

#### Observability in Action

Once instrumented, AX captures complete execution flows:

- *Agent Decision Trees*: Every routing decision from root agent to sub-agents appears as hierarchical traces. You see exactly why the booking agent was chosen over the planning agent.
- *Cost and Performance metrics*:- [Token counts](https://www.youtube.com/watch?v=mpifjVPXPdE)(total, prompt, output, cache, etc.), costs based on your specific model and version (customizable cost tables).
- *Tool Usage Analytics*: Track success rates and latency for every tool. Identify which Google Places API calls succeed, where flight searches fail, and how often hotel bookings time out.
- *Cross-Agent Communication*: When the booking agent needs information from planning, Arize captures these handoffs. You can optimize coordination patterns and identify bottlenecks.

The platform provides graph views showing agent execution patterns, Sankey diagrams for flow visualization, and trace-level inspection for debugging specific interactions.

![google adk travel ai agent graph view in arize ax](https://arize.com/wp-content/uploads/2025/11/adk-travel-concierge-google-agent-graph.png)

![](https://arize.com/wp-content/uploads/2025/11/adk-inspect-path-with-evaluation-metrics.png)

### Automated Agent Evaluation

Observability collects all the important data that we need to evaluate as the next stage in the process. However, standard LLM evaluation isn’t enough for multi-agent systems. [Multi-agent systems require specific evaluations](https://arize.com/ai-agents/agent-evaluation/) suited for its use case. For our travel concierge, Arize AX provides specialized evaluations such as:

- Agent Handoff Quality – Did agents correctly transfer to appropriate sub-agents?
- [Tool Selection Accuracy](https://arize.com/docs/phoenix/evaluation/running-pre-tested-evals/tool-calling-eval)– Did agents choose appropriate tools for the task?
- [Agent Trajectory](https://arize.com/docs/phoenix/evaluation/running-pre-tested-evals/agent-path-convergence)– Did the agent’s entire trajectory follow a logical sequence of steps to fulfill the user’s request?

Online task evaluations automatically run on traces when they arrive into the Arize AX platform, which can also be configured to automatically curate regression/failure datasets reducing time to improvement workflows.

![](https://arize.com/wp-content/uploads/2025/11/agent-handoff-agent-trajectory-evals-on-root-agent-span.png)

![](https://arize.com/wp-content/uploads/2025/11/automated-online-evaluation-setup-for-agent-tool-selection-correctness.png)

### Agent Improvement and Experimentation

After observability and evaluation stages, we now have the critical components needed to affect positive change to our mulit-agent system. [Traces are automatically captured, evaluated, labeled](https://arize.com/resource/llm-tracing/). Regression traces are flagged and sent to datasets. These datasets can be mapped to labeling queues in Arize AX for [human review and annotation](https://arize.com/docs/ax/evaluate/human-annotations) to create [golden datasets](https://arize.com/resource/golden-dataset/).

Users can now run experiments on traces to change agent behavior through Arize’s prompt playground. Arize’s prompt playground enables:

- *Comparative Testing*– Test with different agent instructions or swap models and view outputs side-by-side, measuring impact on decision quality and efficiency.
- *Tool Description Refinement*– Since agents rely on tool descriptions for selection decisions, optimize these based on actual usage patterns and success rates.
- *Dynamic Prompt Optimization*– Production data reveals patterns in user requests. Use these to optimize agent prompts for common scenarios. Teams can run A/B tests on datasets before deployment, comparing different prompt versions, model configurations, and evaluation strategies.

In our travel concierge example, our “valid destination evaluator” identified traces where user queries contained travel requests to impossible destinations (for example Mars, Saturn, Hogwarts, etc.). Our online evaluator automatically flagged these regressions and saved those traces into a curated dataset “travel concierge failures.”

![](https://arize.com/wp-content/uploads/2025/11/finding-invalid-label-arize-ax.png)

Experiment and A/B test with various system prompt and model changes in prompt playground. Validate the changes at scale by running the experiments on the regression dataset from the previous step.

![](https://arize.com/wp-content/uploads/2025/11/prompt-testing.png)

![](https://arize.com/wp-content/uploads/2025/11/adk-experimentation-look.png)

![](https://arize.com/wp-content/uploads/2025/11/compare-experiments-inspect-llm-adk-outputs-side-by-side.png)

### Proactive Production Monitoring

Evaluation driven improvement is a continuous cycle. As the system scales, new edge cases and insights emerge, driving an ongoing iterative process that evolves over time. Arize AX provides crucial proactive scale monitoring, reporting and alerting:

- *Cost Optimization*– Detailed tracking of model calls, tool usage, and processing time enables cost optimization while maintaining performance. Identify redundant API calls or cases where expensive models handle simple tasks.
- *Anomaly Detection*– The platform automatically identifies unusual patterns in agent behavior, such as sudden increases in tool call failures or changes in decision-making that might indicate model drift.
- *Continuous Improvement*– Production data feeds back into development. Identify edge cases, improve agent instructions, and enhance tool implementations based on real user interactions.

Custom metrics derived from evaluations create executive dashboards and proactive monitoring. Alert stakeholders when important KPIs degrade.

![](https://arize.com/wp-content/uploads/2025/11/dashboards-business-metrics-adk-google.png)

## Conclusion

What we’ve explored through our travel concierge example is more than just a technical integration, it’s a comprehensive solution to the fundamental challenge of building better agents. Google’s ADK provides the sophisticated orchestration capabilities needed to build complex, multi-agent systems that can handle real-world complexity. Arize AX delivers the observability and evaluation infrastructure that transforms these systems from experimental prototypes into reliable business tools. Together, they eliminate the traditional barriers that have kept agent applications in the realm of demos and proof-of-concepts.

Looking ahead, this partnership positions organizations to take advantage of the next wave of AI capabilities. As models become more sophisticated and agent frameworks more powerful, the organizations with robust development and observability practices will be best positioned to capitalize on these advances. The future of enterprise AI belongs to organizations that can build not just impressive demos, but reliable, scalable, and continuously improving agent systems. The Google ADK and Arize AX partnership provides the foundation for that future.
