---
title: 'ShopGym: Realistic, reproducible sandboxes for shopping agents (2026)'
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: shopify
url: https://shopify.engineering/shopgym
author: Mingyu Zhao
published: '2026-10-01'
fetched: '2026-10-03T06:18:21Z'
classifier: null
taxonomy_rev: 2
words: 1280
content_sha256: 68ce981aeccfb429b3185402f895b345668010b9ca9be1590988c15c668e66b7
---

# ShopGym: Realistic, reproducible sandboxes for shopping agents (2026)

A shopping agent might help you find a jacket within your budget, choose the right size, check the return policy, and add it to your cart. That part feels easy, but training and evaluating these agents is challenging because products, prices, and store layouts keep changing. Bot detection and throttling can also interrupt runs, while hand-built test stores offer control but capture only a limited range of shopping experiences.

This led us to ask: **Can we make shopping environments repeatable without losing the complexity of real stores?**

We built **ShopGym** to answer that question. It turns live storefronts into self-contained, resettable sandbox shops and generates shopping tasks tied to their products, features, and policies. Developers can reproduce failures, compare agents under consistent conditions, and measure whether changes improve performance.

This also benefits merchants. Our goal is to build shopping agents that work reliably across stores of all sizes and categories, from clothing and digital goods to home improvement. These environments give agents a place to practice finding products, understanding store policies, and completing shopping tasks before interacting with live stores.

![High-level ShopGym architecture](https://cdn.shopify.com/s/files/1/0779/4361/files/ShopArena.png?v=1790799290)

*Fig 1: High level ShopGym architecture*

## From live storefronts to repeatable benchmarks

ShopGym bridges this gap with two parts. Its simulation layer, ShopArena, converts live seed storefronts into self-contained sandbox shops through anonymized shop specifications and a staged, validated generation process. On top of these storefronts, ShopGuru synthesizes benchmark tasks across seven skill categories, grounding each task in the shop's catalog, navigation structure, policies, and interaction affordances.

We validated the framework with graph-based structural analysis and agent-based behavioral evaluation over 224 tasks across six sandbox shops, three built from synthetic data and three from real data. The synthetic shops preserve key structural properties of live storefronts, and agent performance on synthetic shops positively correlates with performance on the live storefronts they mirror.

![Generated sandbox shops](https://cdn.shopify.com/s/files/1/0779/4361/files/Sandbox_shops.png?v=1790799471)

*Fig 2. Screenshot of generated sandbox shops*

You can explore the generated sandbox shops on the [ShopGym project site](https://shopgym-research.github.io/#shop-carousel), with examples spanning clothing, cookware, electronics, and more.

## How ShopGym works

**ShopGym** consists of two complementary frameworks in one workflow. **ShopArena** builds the environment, and **ShopGuru** builds the benchmark. Both are organized as small sets of coding agents communicating through the file system, with execution–verification loops that keep long-horizon generation reliable.

### ShopArena: live storefronts exploration

ShopArena separates storefront exploration from sandbox generation. A shop specification connects the two phases and serves as their only interface.

Exploration begins with the storefront's key surfaces: its homepage, sitemap, search and cart endpoints, public catalog, and policy pages. A planner agent divides this material into focused tasks.

For each task, ShopArena starts a fresh specification agent with browser tools. The agent explores the seed storefront, captures evidence, and writes an anonymized fragment. Together, these fragments describe three parts of the shop:

1. A design specification describing the shop and its visual style
2. Structured attributes for features like filters, navigation, and pagination
3. Catalog statistics including product counts and price distributions

While writing, the agents omit brand names, product names, people's names, and absolute URLs. Every later stage therefore stays anonymous without a separate redaction pass.

A consolidation step then merges the fragments into one specification. ShopArena can also combine specifications from several seed shops, giving one sandbox more structural and behavioral variety than any single source.

Because the specification is readable, benchmark creators can inspect or edit the environment without revisiting the source storefront.

![Planning agent](https://cdn.shopify.com/s/files/1/0779/4361/files/Planning_agent.png?v=1790799519)

### ShopArena: sandbox generation

The generation phase reads only the specification, never the source material collected during exploration. ShopArena first uses the specification’s design details and catalog statistics to generate a fictional product catalog, including collections, product names, descriptions, and images. It then builds the storefront in a fixed sequence: site shell and homepage, collections, product pages, cart, search and filtering, policy pages, and a final integration pass. Each step builds on stable work from earlier steps. If a feature fails, ShopArena can repair it without regenerating the whole shop.

Every step runs the same execution and verification loop:

1. A fresh execution agent reads the current code, relevant specification, catalog, and latest feedback
2. The agent edits the code and runs lightweight checks, including type checks and builds
3. Rule-based checks verify the build, required routes, and output structure
4. A visual verification agent hosts the shop, inspects it in a browser, and writes feedback for the next iteration

Starting a fresh agent for each iteration keeps its working context small. The source code holds the current state, the specification holds the intent, and then the latest report describes the next repair.

![Shop specifications](https://cdn.shopify.com/s/files/1/0779/4361/files/Shop_specifications.png?v=1790799555)

### ShopGuru: task generation

ShopGuru creates shopping tasks using each sandbox shop’s products, navigation, filters, and policies. Some tasks test a single skill, such as finding a specific product or locating the return policy. Others combine several steps, such as opening a collection, filtering by color, sorting by price, and adding a matching product to the cart.

Rule-based generators create the simpler tasks, while an LLM writes the multi-step journeys. Automated checks verify that the products, collections, and filter options referenced in each task exist in the shop. When a task fails these checks, the LLM receives feedback to revise it.

![Shop data](https://cdn.shopify.com/s/files/1/0779/4361/files/Shop_data.png?v=1790799585)

## Evaluation generated sandboxes

We tested ShopGym in two ways. First, we compared the structure of real and synthetic shops. Then we measured how agents behaved in both. To recap, the study covered 224 tasks across six sandbox shops: three with synthetic data and three twins with real product data.

### Structural fidelity

We compared real and synthetic shops by mapping their pages and interactive states, such as open menus and cart drawers, into graphs. The left panel shows an example: nodes represent interface states, and arrows represent actions that move between them. The middle panel compares the number of states and connections, while the right compares page structure and available controls.

![Three visualizations](https://cdn.shopify.com/s/files/1/0779/4361/files/3_visualizations.png?v=1790799612)

Synthetic shops have a similar number of distinct states and comparable page complexity. They have fewer connections between states, largely because they omit external links, marketing pages, and other auxiliary paths found on live stores.

### Behavioral alignment

To test our six sandbox shops, we used two evaluation systems: BrowserGym with accessibility-tree observations, and an internal system that also uses screenshots. Each chart compares success rates on live stores and twins for focused tasks and multi-step shopping journeys.

![](https://cdn.shopify.com/s/files/1/0779/4361/files/4_bar_charts.png?v=1790799648)


Similar success rates suggest that the twins retain useful difficulty from the live stores. This alignment is clearest on multi-step tasks, where both systems also preserve the model ranking. Some focused tasks show larger gaps, particularly in the internal system, so the twins do not reproduce live-store difficulty exactly.

## Working toward more capable shopping agents

ShopGym shows that reproducibility doesn’t have to come at the cost of realism. We can give shopping agents a stable place to fail, learn, and improve while preserving meaningful signals from the live web.

You can explore the generated sandbox shops on the [ShopGym project site](https://shopgym-research.github.io/#shop-carousel), with examples spanning clothing, cookware, electronics, and more.

Next, we plan to generate more sandbox shops across a wider range of retail domains, create more tasks for each shop, and support new task types that cover more of the shopping journey. Our study tested the quality of the generated stores and shopping tasks. We have ongoing work using these environments to train shopping agents.

Together, the goal of these efforts is to turn ShopGym from a framework for simulation and benchmarking into a platform for building more capable shopping agents for merchants and buyers.

\*\*\*\*\*\*

*This article contains contributions from Chinmay Savadikar, Yuanzheng Zhu, Han Li, Shuang Xie, Alberto Castelo, Tianfu Wu, Lingyun Wang.*
