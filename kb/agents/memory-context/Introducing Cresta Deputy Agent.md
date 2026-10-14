---
title: Introducing Cresta Deputy Agent
kind: blog
topic: agents
subtopic: memory-context
secondary_topics:
- product-engineering/case-studies
summary: Cresta's Deputy Agent is a long-running agent for customer-ops workflows
  (insurance claims, order returns, billing disputes) that persists goal, completed
  actions, and dependencies across pauses lasting days to weeks, resumes on new documents
  or approvals, and distinguishes an initiated action from a confirmed outcome with
  a full audit trail.
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/meet-deputy-agent-a-long-running-ai-agent-built-for-customer-operations
author: Ping Wu
published: '2026-10-13'
fetched: '2026-10-14T06:09:48Z'
classifier: claude
taxonomy_rev: 2
words: 1469
content_sha256: 537cb4095494af37537966247df80a4284f39a25a0bec8cb68a41729196b1b93
---

# Introducing Cresta Deputy Agent

A single customer call can set off days of work across multiple teams and siloed systems.

Take a homeowners insurance claim that starts on a call.

The agent would need to log into the claims system and check coverage in a separate policy system. They’d go on to assign the claim to an adjuster, who chases the customer for documents and stores them in a document management system.

Once the adjuster finishes, a manager may need to approve it, often by email, before finance issues a payment in the accounting system and updates the claim record.

That’s at least four teams working in four systems. It’s little surprise that the [average homeowners insurance claim takes about 41 days](https://www.jdpower.com/business/press-releases/2026-us-property-claims-satisfaction-study/) to go from reported to paid.

Now take a customer who calls a retailer to return an online order.

The agent has to find the purchase in the order system, confirm it’s within the return window, and create a return authorization in a separate returns platform.

Returns that are high value or look off go to loss prevention or a supervisor, usually by email. And only once it’s signed off does finance release the refund to the original payment method and book the credit in the accounting system.

The high cost of executing returns is *the* [leading reason](https://nrf.com/media-center/press-releases/consumers-expected-to-return-nearly-850-billion-in-merchandise-in-2025) why retailers charge for them.

You’ve probably tried to automate tedious, long-running workflows like these before with robotic process automation (RPA) software or LLMs and agent builders.

But neither can start the job during the customer’s call, see it through across your systems and teams, and confirm it’s finished. RPA only follows fixed steps with no understanding of the customer, and it never sees the conversation at all. LLMs and agent builders can reason, but their access to your conversations is limited. They can’t follow a customer’s full journey across every human-led and AI-led interaction as it happens, so they miss moments when work should start and can’t carry it through every conversation where it continues.

That’s why we built [**Cresta Deputy Agent**](https://cresta.com/deputy-agent).

## **Built to Execute Work, End to End**

Deputy is a long-running AI agent that automates customer experience workflows from start to finish for as long as it takes to get the job done. It works alongside employees during live interactions, takes handoffs, or runs independently in the back office.

Deputy remembers the goal, what’s been done, what information still needs to be provided, and what needs to happen next. It preserves that context and progress through pauses, whether the work takes a few minutes or several weeks.

When a document arrives, an approval is given, or another condition is met, Deputy resumes from where it left off. And when an approval is what's holding work up, Deputy provides the approver with the case details and supporting evidence they need to decide, instead of leaving them to reconstruct the case across systems.

For your business, that means greater operational capacity, lower manual processing costs, and fewer gaps that create delays, rework, and risk. For your customers, it means follow-through without having to manage every next step.

Deputy is built for the workflows that eat up the most time behind the scenes, and have to move through multiple systems and people before they're actually resolved.

## **How Deputy Works**

We’ll take a closer look at how Deputy can support your teams across three modes of workflow automation.

#### **1. Automate work alongside employees as the conversation unfolds**

While a customer talks to one of your human or AI agents, Deputy listens for the moments that require a workflow to be started.

When it recognizes a condition you’ve defined, or when an agent kicks off a workflow directly, it starts handling the operational steps in the background. Your business rules decide which actions happen automatically and which wait for review.

This happens through [Agentic Assist](https://cresta.com/agent-assist), Cresta’s real-time guidance for human agents, which is how Deputy sees the conversation as it unfolds and acts alongside the person handling it.

Say a customer raises a complaint on a call. Deputy detects it, captures the relevant details from the interaction and your connected systems, classifies it, and creates and routes the case to the right team. The agent never opens a ticket by hand or re-enters a detail the customer already gave.

That means more attention on the customer and less of the repetitive work that drives up handle time, after-call work, and downstream errors.

#### **2. Carry context and work beyond the conversation**

Deputy can also handle the critical business processes triggered by something that happens in a conversation, but requires additional follow-up, paperwork, or handling by specialists to close the loop. For example, if a borrower calls to complain that their account was reported late to the credit bureaus when they’d paid on time, Cresta AI Agent can capture the details and log the complaint during the call, then pass the context and remaining work to Deputy.

Deputy gathers supporting information from connected systems and prepares the complaint for review, bringing together the relevant case details and evidence. When human input or approval is needed, Deputy can pause without losing context, then resume the workflow based on the information or decision provided.

Deputy can also pick up work from more than one conversation with a customer.

Say a customer calls about a charge they don’t recognize. Cresta AI Agent captures the details, opens a dispute, and hands the case to Deputy, which pulls the account history and transaction records from separate systems, finds that a receipt is missing, and pauses the case while it waits.

Two days later, the customer calls back with the receipt. This time, the agent hands off the new information to Deputy, which attaches it to the existing case instead of starting over, compares it against the charge, and sends the adjustment to a manager for approval. Once it’s approved, Deputy processes the adjustment, updates the record, and tells the customer the outcome.

#### **3. Execute back-office workflows through to the desired outcome**

Not every workflow starts with a customer on the line. Some of the most time-consuming work in your operation begins when a document lands in a queue, an account changes status, or a scheduled review comes due. Deputy can pick up that work too, with no conversation involved.

Say a borrower pays off their loan and the account closes with a credit balance, which drops a refund request into a servicing queue. Deputy confirms the payoff posted, verifies the overpayment against the account history, and prepares the refund for approval. If a required record is missing, Deputy can complete the available steps and resume once outstanding requirements are met.

Deputy’s saved workflow state preserves the goal, context, completed actions, and dependencies, and it distinguishes an initiated action from a finished outcome. Submitting a refund, for example, isn’t the same as confirming that payment succeeded.

The value isn’t simply that AI can run longer. It’s that people don’t have to check statuses, chase dependencies, and coordinate every next step.

## **See Every Workflow, Govern Every Action**

With Deputy, every workflow is visible and every action is governed.

You can see which workflows are running, what step each is on, what actions Deputy has taken, and where someone needs to step in.

You also decide how Deputy works. Set rules that define what it can do on its own, what needs approval before it proceeds, and who can intervene along the way. When a decision does need a person, Deputy gives the reviewer all of the information they need in one place, so they can decide without searching across systems.

Every action and approval is recorded in an audit trail. This lets your team trace how a request was handled, and whether the work ran during a live conversation, after a handoff, or entirely in the back office.

## **A New Layer, Not a New Silo**

Cresta is building the AI operating system for customer experience, connecting customer understanding, human assistance, and automation on one platform.

Deputy only adds to Cresta AI Agent and Agentic Assist. Cresta AI Agent handles customer conversations and requests, while Agentic Assist helps employees serve customers in real time. And Deputy takes on the operational workflows that support those experiences, whether the work happens during an interaction, continues afterward, or never involves a conversation at all.

Deputy carries forward the relevant information, decisions, and progress, then gathers what it needs next. A customer response, a new document, or a human approval becomes part of the ongoing workflow, not another handoff someone has to reconstruct.

People stay in the process. Your business sets the rules, grants the approvals, and defines what counts as done. Deputy does the work in between.

Less chasing. More follow-through.

See Deputy in action in our upcoming webinar: [register now](https://na2.hubs.ly/H08kkZm0)!
