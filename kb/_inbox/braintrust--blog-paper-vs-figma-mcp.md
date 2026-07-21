---
title: Paper MCP vs Figma MCP for frontend agents - Blog - Braintrust
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: braintrust
url: https://www.braintrust.dev/blog/paper-vs-figma-mcp
author: Braintrust Team
published: '2026-07-20'
fetched: '2026-07-21T06:50:36Z'
classifier: null
taxonomy_rev: 2
words: 4090
content_sha256: fe058e1f731a470a1abd7700e47f220daf62298f56e9e31d7267886b63ddcb6c
---

# Paper MCP vs Figma MCP for frontend agents - Blog - Braintrust

20 July 2026Jess Wang21 min

A design MCP server gives a coding agent the tools of a design program, so it can lay out a page on the canvas and read that design back as frontend code. The premise is that an agent working this way builds better frontends. The [Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/) is most designers' default server platform, and the [Paper MCP server](https://paper.design/docs) is a newer design tool.

Figma was built for humans clicking in a canvas, and under the hood it stores designs in its own proprietary format. So an agent designing in Figma works through a translation layer, turning its intent into Figma shapes and then exporting that back out to code, either by copying CSS out of Dev Mode or by mapping components through Code Connect, Figma's system for linking design components to the ones in your codebase. That step is imperfect by definition, because the gap between Figma's component model and your production framework has to be bridged somewhere. And the newer direction, an agent pushing design onto the canvas instead of reading it out, is still in beta.

Paper is newer, and its canvas is HTML and CSS. There's no proprietary format in the middle. The agent designs by writing the same code it will eventually ship, and when it reads the canvas back it gets the actual CSS values on each element. A card on the canvas is already a div with CSS, and Paper's `get_jsx` tool hands it back as component code directly.

I ran an independent eval to test which MCP server is better. Here is what I found.

- Paper holds its quality across page types, while Figma drops on the complex designs. Paper barely moves from simple pages to complex ones while Figma slips further, though the two still tie on average and Figma's drop traces to a couple of designs where it collapsed outright rather than a broad weakness.
- On ordinary webpages, the design MCP doesn't matter. On visual similarity, a 0 to 1 score of how closely the recreation resembles the original (1.0 is identical), Paper averages 0.741 and Figma 0.744 across 40 pages.
- On complex, design-heavy pages, the tools tie too. Across 27 designs, Paper averages 0.716 and Figma 0.679, and the paired difference does not clear significance (p = 0.21).
- Where the tools genuinely separate is consistency and price. Figma's run-to-run variance is about 1.9 times Paper's, and it runs 42% longer while costing 32% more per point of visual quality ($3.73 vs $2.82).
- Both agents developed visual self-correction unprompted, screenshotting their own canvas to compare against the reference. But across 160 runs, the correlation between how often an agent checked and how good its page came out is effectively zero.
- The two tools write different HTML dialects. Figma produces semantic tags at over 3 times Paper's rate.

For each run, the agent gets a screenshot of a webpage and must recreate it as a single self-contained HTML file. The prompt requires building the design in the MCP tool first, then deriving the HTML, because early smoke tests showed agents skip design tools entirely when given the choice. Each variant sees exactly one MCP server, enforced with strict MCP config.

**Dataset one, simple pages:** [Design2Code](https://huggingface.co/datasets/SALT-NLP/Design2Code-hf), the academic benchmark from Stanford's SALT-NLP lab. It includes real webpages sampled from Common Crawl, each with a screenshot and ground-truth HTML. It's the standard in screenshot-to-code research (the [companion repo](https://github.com/NoviScl/Design2Code) has 586 stars, and follow-up benchmarks measure against it). However, these pages predate modern design trends. One thing to know before you look at the sample below is that Design2Code strips the real photos out and replaces them with solid blue placeholder boxes, and the agents are told to treat those boxes as placeholders. I sampled 40 pages from the benchmark with a fixed random seed, so the subset is arbitrary but reproducible.

![Contact sheet of 15 of the 40 sampled Design2Code pages, each labeled with its benchmark page number. The set includes forum threads, artist portfolios, documentation sites, personal blogs, small-business pages, and quote and jokes sites. Many pages contain solid blue rectangles where photos would be.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/design2code_sample.png)


**Dataset two, complex designs:** 27 pages I hand-picked for the textures that stress CSS-first workflows like glassmorphism, 3D-rendered elements, volumetric glow, dense dashboards, and display typography. The set mixes shots from [dribbble](https://dribbble.com) and hero sections from live sites. No ground-truth HTML exists for these, so the reference screenshot doubles as the scoring target. Because 27 designs is still a small dataset, each one ran three times per tool, and every number reported below is the mean across those trials, which steadies the estimates and turns run-to-run consistency into a measurable finding of its own.

![Contact sheet of all 27 complex designs with their short names: agentcard, aiaf (3D robots), amanah (CRM dashboard), bronn, canton, chenard, defi (glass hero), drone (fire dashboard), food (app phones), games, grocer, horsecare, inspirux, kaiko, liquid (glass swap widget), lydia, med, medium (bold type stack), nirnor, park (flat illustration), radial (topic graph), sondaven, spatial, stageone, supari, units, and worldbuild.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/design_legend.png)


| Scorer | Type | What it checks | 
|---|---|---|
| `render_success` | deterministic | The HTML renders to a non-blank page in headless Chrome | 
| `visual_similarity` | deterministic | CLIP embedding similarity between the rendered output and the reference screenshot | 
| `recreation_faithfulness` | LLM judge | Binary judgment of whether someone who knows the original would recognize this | 
| `text_content_recall` | deterministic | Fraction of the original's visible text present (ground-truth pages only) | 
| `dom_structure_similarity` | deterministic | Tag-tree similarity to the original markup (diagnostic only) | 

[CLIP](https://github.com/openai/CLIP) is a model from OpenAI that maps images into a numerical space where similar-looking images land close together. The closeness of the two image vectors becomes a 0 to 1 score. The judge runs claude-sonnet-5 at temperature 0 with both screenshots in one message. Its prompt, verbatim:

You are comparing two webpage screenshots. Image 1 is the ORIGINAL webpage. Image 2 is an attempted RECREATION. Question: would someone familiar with the original page recognize the recreation as that page? Judge on: overall layout structure, content hierarchy and placement, color scheme, and presence of the main sections and content. Ignore: font-rendering differences, minor spacing, and placeholder images standing in for real photos. Respond with JSON only:

`{"faithful": "yes" | "no", "reason": "<1-2 sentences>"}`

One calibration step I'd recommend to anyone building visual evals is to feed your scorers a known-perfect answer first. I scored the dataset's own ground-truth HTML against its own screenshot. It got 1.0 on everything except visual similarity, where it got 0.93. Even a pixel-perfect recreation can't hit 1.0 on CLIP, because re-rendering produces slightly different pixels. So 0.93 is the real ceiling, and an agent at 0.85 is closer to perfect than it looks.

Each eval row spawns a fresh Claude Code session as a headless subprocess with exactly one design MCP attached. The whole comparison comes down to a few flags. `--strict-mcp-config` guarantees the agent sees only its assigned server, and the tool allowlist is identical for both variants.

python

```
cmd = [
    "claude", "-p", prompt,
    "--model", "claude-sonnet-5",
    "--mcp-config", f"{variant}.mcp.json",   # exactly one design MCP
    "--strict-mcp-config",
    "--allowedTools", f"Read,Write,Edit,Bash,mcp__{variant}",
    "--permission-mode", "acceptEdits",
    "--output-format", "stream-json", "--verbose",
    "--settings", "trace.settings.json",     # tracing config, below
]
proc = subprocess.run(cmd, cwd=workdir, env=scrubbed_env, timeout=1500)
```
Tracing happens at two levels. The `Eval()` run logs each row to a Braintrust experiment with its scores, the rendered screenshot next to the reference, and tool-usage counts. For the agent's internals, the [trace-claude-code plugin](https://github.com/braintrustdata/braintrust-claude-plugin) hooks every turn and tool call inside the subprocess and streams them to Braintrust, so you can open any run and read each MCP call with its inputs and outputs. One caveat is that the plugin writes to the project's logs, not into the experiment itself, so the harness stitches the two together by putting a permalink to the agent's full internal trace in each experiment row's metadata.

python

```
span.log(metadata={
    "tools_used": tools,
    "mcp_tool_calls": mcp_calls,
    # plugin traces land in Logs, not the experiment,
    # so link each row to its agent's internal trace
    "agent_trace_url": f"{APP_URL}/logs?r={session_id}",
})
```
![A Braintrust trace view of one eval row. The span tree on the left shows the agent_run span with its scorers (render_success, visual_similarity, recreation_faithfulness, design_effects_fidelity). The details pane on the right shows the span's metadata, with agent_trace_url highlighted, a link into the project's logs, alongside mcp_tool_calls (14), num_turns (42), and session_id.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/experiment-trace-metadata.png)


Every claim in this post about what agents did mid-run (from the self-check loops to what happened during failed runs) comes from reading those traces.

| Metric | Paper | Figma | 
|---|---|---|
| Visual similarity | 0.741 | 0.744 | 
| Faithfulness (judge) | 0.975 | 1.000 | 
| Text recall | 0.821 | 0.821 | 
| Render success | 100% | 100% | 

Remember all scores run 0 to 1, higher is better, and that the visual similarity's practical ceiling is 0.93. Though the results ended in a tie, the traces were more interesting than the scores. Two behaviors stood out.

**Both variants developed visual self-correction.** Unprompted, agents screenshot their own canvas and compare against the reference. Paper agents did this 3.4 times per session, Figma agents 2.4 times. The agents treat the design tool as a feedback loop, not only an output surface.

![A Braintrust trace of one agent session, showing a span tree of Paper MCP calls. Arrows mark the repeated get_screenshot spans interleaved between write_html, get_node_info, and delete_nodes calls. The detail pane shows a write_html call with inline CSS.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/selfcheck-trace.png)


**The tools produce different HTML dialects.** Figma's pipeline writes semantic HTML5. Paper's iterative canvas approach produces layouts built almost entirely from generic `<div>`s.

html

```
<!-- figma -->
<header class="topbar">
  <p>Stage One contract acts as…</p>
  <div class="brand"><span class="icon"><svg …>
```
html

```
<!-- paper -->
<div class="top-bar">
  <p>Stage One contract acts as…</p>
  <div class="brand-mark"><svg class="house-icon" …>
```
Across the 248 HTML files the agents produced over the course of the eval, including retried runs, Figma uses semantic tags at over 3 times Paper's rate. Paper's output is 46% `<div>`s to Figma's 35%. Both render identically well.

A `<div>` is a generic box that says nothing about its contents, whereas semantic tags like `<header>`, `<nav>`, and `<main>` declare what the content is. They look identical on screen, but machines read them differently. Screen readers use semantic tags as landmarks, so someone relying on one can jump straight to the main content instead of stepping through every box on the page (class names like `top-bar` don't help, because assistive tech ignores them). A developer opening the file months later gets the page's architecture easily instead of reverse-engineering it from class names.

So essentially, Figma's generated code is the more accessible and more maintainable of the two in this eval, even though both sets of pages render the same.

Here are the numbers across all 27 designs at three trials each.

| Paper | Figma | |
|---|---|---|
| Visual similarity | 0.716 ±0.027 | 0.679 ±0.043 | 
| Faithfulness (judge) | 0.728 | 0.654 | 
| Render success | 100% | 100% | 
| Duration per run | 400s | 568s | 
| Cost per run | $2.02 | $2.53 | 
| Cost per quality point | $2.82 | $3.73 | 

![Grouped bar chart: visual similarity for Paper and Figma on simple pages and complex designs. Paper scores 0.741 on simple pages and 0.716 on complex designs. Figma scores 0.744 and 0.679. Error bars overlap on the complex side. A dashed line marks the metric ceiling at 0.93.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/p0_headline_quality.png)


**On visual similarity, this is a tie as well, just a more textured one.** Paper's average visual similarity sits a few hundredths above Figma's, and the paired test across the 27 designs puts the gap at +0.038 with p = 0.21, meaning a difference this size would show up about 21% of the time even if the tools were genuinely equal. That is nowhere near the conventional 5% significance bar, so the defensible claim is that the tools are statistically indistinguishable on average visual quality here. The average alone misses the shape of the distribution. The two largest per-design margins in the entire eval both belong to designs where Figma collapsed outright, the 3D robots (aiaf) and the flat illustration (park), while everywhere else the margins are small and go in both directions. Figma has occasional collapse modes on specific design types rather than a general weakness on complex pages, and the two tools otherwise tie.

Since those two collapses drive the shape of the whole comparison, I read all six of those Figma traces to see what happened. On park, all three trials collapsed the same way (0.09, 0.20, and 0.04). The agent built the full illustration correctly (the bridge, the sunburst, the court, the lettering) then created an HTML page where that artwork renders as a small badge floating in an empty canvas. The agent got the content right and the scale wrong. This is because a Figma composition has a fixed frame size and nothing forces it to fill a browser viewport when it becomes HTML. Two of those trials self-checked six and eight times and still shipped the miniature, which makes sense once you notice that the checks screenshot the Figma canvas, where the composition genuinely looks right. On aiaf, the story is variance rather than repeatable failure. Two trials landed around 0.44 with the robots flattened but the page structure intact, and one went down to 0.09 by rendering the whole page as a narrow column surrounded by empty space. Paper, whose canvas is already a viewport-shaped HTML page, never produced either failure mode.

**Where the tools genuinely separate is consistency and price.** Figma's output varies about 1.9 times as much from one run to the next as Paper's. Given the same design and the same prompt, Paper produces roughly the same page each trial, while Figma's quality swings more between draws. Figma also runs 42% longer and costs 32% more per point of visual quality. Also, while CLIP reads the tools as a tie, the judge preferred Paper's recreations (0.728 to 0.654). The paired faithfulness gap is +0.080 at p = 0.17, so it isn't significant either, but it leans consistently toward Paper.

![Bar chart of per-row standard deviation across three trials for each of the 27 designs. Figma's bars are taller than Paper's on most rows, with several above 0.15 while Paper mostly stays under 0.05.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/p4_trial_variance.png)


The self-correction behavior turned out not to help on the complex designs either. Across the 160 complex-design runs where the harness captured self-check counts (a few runs lost that telemetry to logging failures), the correlation between how many times an agent checked its own canvas and its final visual similarity score is r = +0.01 for Paper and r = −0.19 for Figma, and neither is statistically meaningful. So the self-checking does not translate into a better page. If anything, the Figma agents that check the most tend to be the ones struggling with the hardest designs, which is why that relationship, to the extent there is one at all, leans slightly negative.

![Scatter plot of self-check screenshots per run against visual similarity for both variants. Points form a flat cloud with no upward trend.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/p1_selfcheck_scatter.png)


Breaking the results down design by design shows where each tool wins, and the size of each margin matters as much as its direction. On most of the 27 designs the two tools finish close together, with small wins scattered in both directions. The two huge margins are the 3D robots (aiaf) and the flat illustration (park), where Figma broke down. On the park illustration in particular, Figma's three trials averaged 0.11, which means its recreations barely resembled the target at all. No other design comes close to either collapse, in either direction.

![Dumbbell chart of mean visual similarity per design across all 27 designs. Each design is a horizontal line with a dot for Paper and a dot for Figma. Most margins are small, with wins in both directions. Two designs show huge Paper margins, aiaf at +0.38 and park at +0.58, where Figma's scores collapse.](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/p3_dumbbell.png)


On the park illustration, Figma reproduced the artwork but shrank it into a small thumbnail stranded in empty space, while Paper rebuilt the whole poster at full scale. That single difference accounts for most of the 0.58 gap on this row.

**park**, flat illustration. Paper 0.69, Figma 0.11.

![Reference poster for Park Padel, a detailed flat illustration filling the frame, next to Paper's recreation at full scale and Figma's recreation, where the artwork is reproduced but shrunk to a small badge floating in empty space](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/park-padel-flat-illustration/triptych.png)


The lowest-scoring designs in the whole eval were not failures of either tool. They mark the limit of what the output medium itself can express. One dribbble page features three 3D-rendered robot heads with brushed metal, chamfered edges, and eyes emitting pink light that reflects off nearby surfaces.

Art like that is never made in a design tool in the first place. The real workflow runs through a 3D program ([Blender](https://www.blender.org/), Cinema 4D, [Spline](https://spline.design/)), where a designer models the objects, assigns materials, lights the scene, and renders the result to an image. On the actual shipped site, those robots are a flat PNG dropped into the page, not code at all. Real design work divides the labor this way, using CSS for structure and layout and pre-rendered images for the parts that need photographic richness.

CSS is a procedural medium, meaning it draws its effects from rules rather than from stored pixels. It is good at frosted glass (`backdrop-filter` plus layered translucent shadows), glow (stacked radial gradients with blend modes), grain, and even refraction through SVG filters. What it cannot do is express photorealistic lighting, metallic reflection, or anything else that a renderer produces by simulating how light actually behaves. When the agents rendered the robots as flat gray shapes, they were running into the boundary of what HTML and CSS can express. It was not a shortfall in their own ability, and a stronger model or more attempts would not have changed the outcome, because the medium cannot produce that image.

I did chase one path that could raise this CSS ceiling. Figma has real shader support in open beta, with WebGPU shader fills for these materials (liquid glass, chrome, aurora), a [first-party gallery](https://shaders.figma.com/), and a complete plugin API that an agent could use to list, import, and apply them. So the whole pipeline exists from end to end. I still couldn't use it in this eval because the beta wasn't enabled on my account, and even with it enabled, shader IDs are scoped to a specific file, so an agent starting from a fresh file has no way to reach them. The capability is close, but it is not yet usable by an agent. Paper, for its part, exposes no material system through its MCP at all. Its canvas is CSS under the hood, so its texture ceiling is the CSS ceiling.

Paper is more consistent run to run and about 30% faster, while Figma costs about 32% more per point of visual quality. The faithfulness judge leaned toward Paper throughout. Figma writes more semantic, more accessible markup, and its worst failures in this eval were collapse modes on specific design types (a flat illustration, 3D character art) rather than a general quality problem.

Diagnosing those collapse modes is the part Braintrust made easy. Every agent subprocess streamed its full internal trace through the [trace-claude-code plugin](https://github.com/braintrustdata/braintrust-claude-plugin), so each experiment row links to every MCP call the agent made, with its inputs and outputs. And because the rendered output and the reference screenshot sit side by side as images in each row, answering questions took a few minutes of opening rows and looking.

If you're building an eval like this one, Braintrust is the AI observability platform that connects evals and observability in one workflow, from the experiment scores down to each agent's individual tool calls. [Get started →](https://www.braintrust.dev/signup)

Below is the full gallery. Each entry shows one of the 27 complex designs, with the reference next to each tool's best recreation out of its three trials. The scores under each design name are the mean visual similarity across trials, the same numbers used throughout the post, while the images show each tool's single best attempt.

**agentcard**, dark hero for an AI-agent debit card. Paper 0.78, Figma 0.82.

![Reference for agentcard, dark hero for an AI-agent debit card, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/agentcard-dark-debit-hero/triptych.png)


**aiaf**, dark landing page with three 3D robot heads. Paper 0.70, Figma 0.32.

![Reference for aiaf, dark landing page with three 3D robot heads, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/aiaf-3d-robots-dark/triptych.png)


**amanah**, tilted CRM dashboard. Paper 0.88, Figma 0.84.

![Reference for amanah, tilted CRM dashboard, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/amanah-crm-dashboard-tilted/triptych.png)


**bronn**, light fintech accounting hero. Paper 0.82, Figma 0.87.

![Reference for bronn, light fintech accounting hero, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/bronn-accounting-light-hero/triptych.png)


**canton**, blue enterprise page with a radial network graph. Paper 0.66, Figma 0.59.

![Reference for canton, blue enterprise page with a radial network graph, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/canton-network-radial-hero/triptych.png)


**chenard**, dark editorial page with book spines. Paper 0.74, Figma 0.72.

![Reference for chenard, dark editorial page with book spines, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/chenard-editorial-books-dark/triptych.png)


**defi**, dark glassmorphism DeFi hero. Paper 0.84, Figma 0.85.

![Reference for defi, dark glassmorphism DeFi hero, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/defi-glass-dark-hero/triptych.png)


**drone**, dark drone fire-monitoring dashboard. Paper 0.68, Figma 0.61.

![Reference for drone, dark drone fire-monitoring dashboard, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/drone-fire-dashboard-dark/triptych.png)


**food**, orange food app on three phones. Paper 0.75, Figma 0.57.

![Reference for food, orange food app on three phones, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/food-app-three-phones-orange/triptych.png)


**games**, puzzle games card grid. Paper 0.84, Figma 0.86.

![Reference for games, puzzle games card grid, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/games-puzzle-card-grid/triptych.png)


**grocer**, flat illustration of grocery bags. Paper 0.87, Figma 0.86.

![Reference for grocer, flat illustration of grocery bags, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/grocer-bags-flat-illustration/triptych.png)


**horsecare**, phone mockup on a wooden rail. Paper 0.70, Figma 0.64.

![Reference for horsecare, phone mockup on a wooden rail, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/horsecare-phone-mockup-wood/triptych.png)


**inspirux**, black and lime editorial hero. Paper 0.69, Figma 0.69.

![Reference for inspirux, black and lime editorial hero, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/inspirux-lime-editorial-hero/triptych.png)


**kaiko**, blue gradient healthcare hero. Paper 0.84, Figma 0.88.

![Reference for kaiko, blue gradient healthcare hero, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/kaiko-clarity-gradient-hero/triptych.png)


**liquid**, glassmorphism swap widget over a grassy field. Paper 0.84, Figma 0.86.

![Reference for liquid, glassmorphism swap widget over a grassy field, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/liquid-swap-glass-field/triptych.png)


**lydia**, blue halftone portfolio hero. Paper 0.62, Figma 0.76.

![Reference for lydia, blue halftone portfolio hero, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/lydia-blue-halftone-portfolio/triptych.png)


**med**, dark typographic page with a small athlete figure. Paper 0.70, Figma 0.64.

![Reference for med, dark typographic page with a small athlete figure, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/med-dark-type-figure/triptych.png)


**medium**, bold stacked type cards. Paper 0.72, Figma 0.72.

![Reference for medium, bold stacked type cards, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/medium-rare-bold-type-stack/triptych.png)


**nirnor**, minimal Japanese page with a particle field. Paper 0.74, Figma 0.63.

![Reference for nirnor, minimal Japanese page with a particle field, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/nirnor-minimal-particle-field/triptych.png)


**park**, green and yellow flat illustration poster. Paper 0.69, Figma 0.11.

![Reference for park, green and yellow flat illustration poster, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/park-padel-flat-illustration/triptych.png)


**radial**, radial topic graph visualization. Paper 0.85, Figma 0.82.

![Reference for radial, radial topic graph visualization, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/radial-topic-graph-viz/triptych.png)


**sondaven**, ASCII halftone artwork of stacked sheep. Paper 0.71, Figma 0.53.

![Reference for sondaven, ASCII halftone artwork of stacked sheep, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/sondaven-ascii-halftone-art/triptych.png)


**spatial**, black and white warped type poster. Paper 0.54, Figma 0.66.

![Reference for spatial, black and white warped type poster, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/spatial-warped-type-poster/triptych.png)


**stageone**, editorial split-screen interior page. Paper 0.54, Figma 0.61.

![Reference for stageone, editorial split-screen interior page, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/stageone-editorial-split/triptych.png)


**supari**, orange illustrated studio hero with cartoon characters. Paper 0.40, Figma 0.47.

![Reference for supari, orange illustrated studio hero with cartoon characters, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/supari-illustrated-studio-hero/triptych.png)


**units**, colorful student housing hero. Paper 0.62, Figma 0.70.

![Reference for units, colorful student housing hero, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/units-student-housing-hero/triptych.png)


**worldbuild**, editorial services table with icons. Paper 0.58, Figma 0.68.

![Reference for worldbuild, editorial services table with icons, next to Paper's and Figma's best-of-three recreations](https://www.braintrust.dev/blog/img/paper-vs-figma-mcp/appendix/worldbuild-editorial-services/triptych.png)
