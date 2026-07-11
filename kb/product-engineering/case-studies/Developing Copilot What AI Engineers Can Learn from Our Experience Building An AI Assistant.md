---
title: 'Developing Copilot: What AI Engineers Can Learn from Our Experience Building
  An AI Assistant'
topic: product-engineering
subtopic: case-studies
secondary_topics:
- agents/tool-use
summary: Arize Copilot case study covering lessons from building an AI assistant for
  data scientists and AI engineers.
source: arize
url: https://arize.com/blog/developing-copilot-what-ai-engineers-can-learn-from-our-experience-building-an-ai-assistant/
author: Sally-Ann DeLucia
published: '2024-07-30'
fetched: '2026-07-11T04:49:14Z'
classifier: codex
taxonomy_rev: 1
words: 2251
content_sha256: 77052346e8efbc211ffd291186a7cbab7e296e0214527b4b1a27f67d8d155355
---

# Developing Copilot: What AI Engineers Can Learn from Our Experience Building An AI Assistant

[Arize Copilot](https://arize.com/blog/introducing-arize-ai-copilot/) began as an ambitious idea: to develop an AI assistant tailored specifically for data scientists and AI engineers. This tool was designed to assist in streamlining their workflows and simplifying complex tasks. Throughout its development, we encountered numerous challenges and learned valuable lessons about developing with LLMs.

Copilot is an interactive tool that helps users troubleshoot and improve their models and applications. It leverages an agentic workflow, performing tasks on behalf of Arize users. When a user asks Copilot a question or provides an instruction, it first hits one of our routers, which then chooses the appropriate skill(s) to address the user’s request. The router contains generalized instructions and important metadata to help the LLM make the right tool call for the user’s question. The prompts for individual skills then contain more in-depth instructions for a given task and the required data. From the tool, Copilot then returns a response to the user, who can interact with the response and ask follow-up questions if needed.

In our next blog, we’ll dive deeper into Copilot’s Architecture and why we made the choices we did.

## Copilot: Lessons Learned

Building applications with LLMs is a complex and challenging journey. The industry is evolving rapidly, and keeping up with best practices is hard. Throughout our development process with Copilot, we encountered numerous obstacles and learned valuable lessons the hard way. This blog will share the insights we gained, focusing on the practical aspects of developing Copilot and the realities of bringing an AI-driven tool to life. Our hope is that by diving into our lessons learned, you can avoid some of the problems we faced and accelerate your own development with LLMs.

## State

If you’re not familiar with a state machine, it’s a mathematical abstraction used to manage the states and transitions of a system. Considering state was crucial for Copilot because troubleshooting workflows and conversations inherently follow a series of states and transitions. By incorporating state management, we could ensure Copilot navigates through workflows and conversations effectively, maintaining context and delivering accurate, relevant responses.

One key decision point was choosing between the Assistant API and the Completions API from OpenAI. The Completions API is quite basic, offering more control over state management, which we found to be crucial for our application. On the other hand, the Assistant API, which doesn’t require passing prior messages due to its built-in statefulness, is considered an improvement but at the cost of reduced control. In the end, control was imperative for our design so we went with the Completions API and handled everything, including state.

## Swapping Models

About halfway through our development process, OpenAI released GPT-4o, boasting improved practical usability. Eager to switch from GPT-4, we did not anticipate the ripple effect this change would have.

We thought we’d get quicker responses, lower costs, and better performance. In reality, it broke all of our prompts. “Faster, cheaper, and frustrating” was probably a better expectation. GPT-4o consistently failed to respond properly to prompts that were optimized and worked great with GPT-4; nearly all our skills were broken. For instance, our model insight skill, which previously provided relevant advice and adhered to specific output formats, started generating irrelevant advice and ignoring the output format instructions.

This would’ve been a perfect time for experiments and datasets, but honestly, we hadn’t gotten there yet. Now, we have experiments in place that help us take a targeted approach and understand exactly what we need to fix (more on that later). Lacking experiments, we resorted to a manual approach: we tested every skill, adjusted, and iterated on the prompts until we successfully restored our performance.

This was definitely a hard lesson to learn. It was one of the most devastating changes we had. We realized that going forward, we needed to be cautious of the effects new models would have and put in place formal testing frameworks to capture the impact of swapping out a model.

## Prompt Templates

Prompt templates are a critical component in any LLM application. Even minor modifications to prompts can significantly influence the outcomes. Getting the LLM to perform as expected can often be challenging. We found that strategies, including the use of delimiters, chain of thought (CoT), and well-defined sections with explicit instructions were crucial for getting the LLM to respond as intended.

When we began developing Copilot, our prompt structure was straightforward: an introduction with objectives and constraints followed by the required data. This setup managed simple requests adequately but often fell short with complex queries and edge cases, leading to issues like hallucinations and overlooked instructions.

To address these challenges, we introduced several enhancements. To start, we implemented a delimiter pattern (e.g., “***”) to help the LLM distinguish between different sections of the prompt. This visual separation aids in better comprehension and adherence to the instructions. We also began using clear section headers and added helper texts for important instructions, marking them with labels such as “IMPORTANT” to draw attention.

Rather than focusing on what not to do, we shifted to providing clear guidelines on what the LLM should do. For instance, we modified our approach to insights:

- **Old Instruction**- **:**“When proposing insights, please limit only to the most glaring insights and avoid providing too much information.”
- **New Instruction**- **:**“Focus on presenting the most critical insights, such as outliers, edge cases, or anomalous behaviors, which represent the most relevant information.”

We found that by giving it guidelines and heuristics on what to do, we drastically improved our results. In addition to this, one of our most crucial learnings is the importance of explicitness. It’s vital to include every detail that you want the LLM to consider, from step-by-step task guides to specific limitations and guidelines. The more precise the instructions, the better the LLM performs.

We also improved the way we presented data or prompt variables within prompts, including descriptions that explain what the data represents and how it should be used. This adjustment has notably improved the effectiveness of our prompts. We’ll dive into more specifics on data and prompt variables later.

CoT has been instrumental in boosting the LLM’s reasoning capabilities. While it does slow down the initial response time (time to first token), the depth and quality of the output generally improve. However, for tasks that require less complex reasoning, we opt out of CoT in favor of basic prompting techniques.

## Function Variables and Injecting Data

Incorporating data into our prompts is a cornerstone for Copilot’s functionality, given its focus on data analysis. From the start, we recognized the need to integrate data into nearly every one of our prompts to enable effective analysis.

Initially, we formatted the data as CSV, but this approach quickly proved problematic. The CSV format often led to misalignments and hallucinations—imagine trying to make sense of data spread across a row in a CSV file yourself; it’s easy to mismatch cells and columns. The LLM encountered similar difficulties. Shifting to a structured format like JSON significantly enhanced performance by providing a clear, organized data structure.

Another critical insight we gained was that less is often more when it comes to data injection. While it’s essential that the LLM has enough data to perform its tasks, too much information can overwhelm it. It is known that LLM do not utilize extended contexts effectively, which can degrade performance. Therefore, it’s crucial to find a balance: provide sufficient data for the task at hand without inundating the system. This balance ensures that the LLM can process and respond to the information effectively.

## Function Calls

Configuring the router to accurately trigger the correct function can be a challenging aspect of working with an LLM. Initially, we had a certain expectation that the LLM would seamlessly pick the appropriate function once everything was set up. However, we quickly realized this was not the case.

To ensure reliability, it’s essential to be explicit when defining a function call. It’s not enough to simply describe what the function does; it’s equally important to specify when it should be used. This clarity assists the LLM—especially in auto mode—to make more accurate decisions.

Descriptive property definitions are also vital. A recurring issue we encountered was the LLM generating hallucinated values for function inputs. To combat this, we started providing highly detailed descriptions and clear instructions that the LLM should not assume values but instead should query the user for confirmation. This approach significantly reduces errors and improves the overall quality of responses by preventing the LLM from making incorrect assumptions about input data.

## Streaming

From the beginning, we knew that streaming was essential to create a dynamic and interactive nature. This feature enables real-time responses and continuous interaction with the LLM, similar to watching ChatGPT respond as if it were thinking out loud. The alternative, waiting for complete responses, could make users wonder if the system was even working and was not a viable option. Thus we began on the journey of supporting streaming.

Building applications on top of streaming involves navigating a delicate balance between processing inputs and managing the stream itself. This complexity is amplified when dealing with JSON, as streaming JSON back results in a string that isn’t fully parseable until the complete string is received, unlike handling simpler strings word by word. Addressing this was one of our most demanding tasks, which required two engineers and a significant investment of time. Through extensive trial and error, as no definitive strategies or “copy and paste” solutions existed, we developed a framework that detects JSON and only returns complete JSON values while continuing to stream text responses. This abstraction allows our prompt engineers to fine-tune LLM responses that interleave structured JSON and streaming text, ensuring the response is parsed correctly and efficiently.

Streaming adds a layer of complexity that requires careful consideration and substantial effort to manage effectively. The challenges encountered highlight an opportunity for further abstraction to simplify the process, making it more accessible and manageable for developers. In the meantime, we suggest you consider your application and needs when choosing your streaming approach.

## User Experience

We set out to give our users a tool that would take the guesswork and manual steps out of troubleshooting and improving their models. Simply put: we thought it should be easier and faster to iterate. We had strong opinions on flows that worked for these tasks, so it was straightforward to convert these into LLM skills. However, how users should interact with the different skills was less clear.

As we developed skills, we realized that while they performed well, provided the right insights, and excelled at their tasks, the chat format lacked luster. At this point, we were confident that we didn’t want Copilot to be exclusively a chat interface. We realized we needed to build UI components to complement our skills if we truly wanted to nail the user experience. Ultimately, this was a customer-facing tool meant to help them, so we had to ensure we put this at the forefront. We couldn’t just build awesome skills; we needed customers to want to use them.

We leaned on our experience building with LLMs to deliver the tools we wanted, how we wanted them. We added chat-based skills that lived in a chat window where users could interact with charts and information returned. Some features made no sense to be in a chat, so we built mini chat components that brought the natural conversation component into our product where users needed them most. It was crucial that these product integrations were purposeful. We included skills in the product only if they made sense and only where they should be.

We also distilled our experience from assisting customers. We understood that when troubleshooting, the question “what next?” often arises. So we answer that for them in the Copilot interface. Once they ask one question, we dynamically suggest what they could do next to facilitate troubleshooting and usage.

## Test, Test, Test

The necessity of testing is a familiar challenge in development—every change to your pipeline requires verification to ensure it isn’t a breaking change. Efficiently managing this continuous testing cycle is crucial, especially when prompt adjustments are frequent.

Datasets, or collections of examples, are invaluable for this process. They allow you to consistently test changes against a stable baseline. Whether it’s a “golden dataset” of scenarios your LLM handles well or a targeted set designed to evaluate specific adjustments, these examples form the backbone of your testing strategy.

Historically, testing might involve laboriously checking inputs and outcomes manually in documents or spreadsheets—a truly dreadful task. To escape this, we leveraged Arize (yes, we had to name-drop, but don’t worry, this isn’t a sales pitch!) datasets and experiments to set up Github Actions. By integrating datasets with automated testing workflows, similar to CI/CD pipelines, we significantly improved our testing efficiency. This setup allows us to quickly assess the impact of changes and maintain high quality standards effortlessly.

## Conclusion

Every challenge is a learning opportunity. By leveraging our experiences, you can approach development with a better understanding and preparedness. We encourage you to experiment, adapt, and evolve your strategies as you integrate LLMs into your applications. Happy building!

## More Resources on Arize Copilot

Check out these demos and resources to get started with Copilot:

- ▶️ Demo: [Prompt Playground with Copilot](https://arize.com/resource/prompt-playground/)
- ▶️ Demo: [Introducing Arize AI Copilot](https://www.youtube.com/watch?v=zEe9JxMoF8U)
- 📚 Docs: [How To Use Copilot](https://docs.arize.com/arize/copilot/how-to-copilot)

Questions? As always, feel free to [reach out in the Arize community](https://arize.com/community/).
