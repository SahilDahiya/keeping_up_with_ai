---
title: How to Prompt LLMs for Text-to-SQL
topic: prompt-engineering
subtopic: structured-output
secondary_topics:
- evals-observability/evaluation
summary: Practical guide to Text-to-SQL prompting, including schema context, output
  constraints, and evaluation considerations.
source: arize
url: https://arize.com/blog/how-to-prompt-llms-for-text-to-sql
author: Sarah Welsh
published: '2023-12-18'
fetched: '2026-07-11T04:48:07Z'
classifier: codex
taxonomy_rev: 1
words: 5528
content_sha256: 1244bd28de3a04906a6b57a83a12dc99866267fba550860368aefb5b2d0ad2fa
---

# How to Prompt LLMs for Text-to-SQL

![Text to SQL blog image Profile images for Shuaichen Chang and Amber Roberts](https://arize.com/wp-content/uploads/2023/12/Text-to-SQL-blog-image-1021x560.jpg)

              # How to Prompt LLMs for Text-to-SQL

## Introduction

For this paper read, we’re joined by Shuaichen Chang, now an Applied Scientist at AWS AI Lab and author of this week’s paper to discuss his findings. Shuaichen’s research (conducted at the Ohio State University) investigates the impact of prompt constructions on the performance of large language models (LLMs) in the text-to-SQL task, particularly focusing on zero-shot, single-domain, and cross-domain settings. Shuaichen and his co-author explore various strategies for prompt construction, evaluating the influence of database schema, content representation, and prompt length on LLMs’ effectiveness. The findings emphasize the importance of careful consideration in constructing prompts, highlighting the crucial role of table relationships and content, the effectiveness of in-domain demonstration examples, and the significance of prompt length in cross-domain scenarios.

## Watch

Dive in:

Listen:


🎧 **SUBSCRIBE** [Spotify](https://open.spotify.com/show/4sykmDkrUklwyjOCB8FdLQ) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/toolformer-training-llms-to-use-tools/id1666375694?i=1000605075518) | [YouTube](https://www.youtube.com/watch?v=pSKHDduKt_g)

## Transcript

### Overview of the Research

**Amber Roberts:** All right looks like folks are starting to join. I’ll start out with introductions. My name is Amber. I’m a ML Growth Lead. I work a lot with the marketing and engineering team to create content and material around what we’re doing here at Arize and with our open source tool, Phoenix.

I’m very happy to have Shuaichen on this community paper reading. Would you mind giving an introduction?

**Shuaichen Chang:** Yeah, sure. Hi, everyone. I’m Shuaichen Chang. I’m a research scientist at the AWS AI lab. And before this, I was doing my PhD at the Ohio State University. So my research is about natural language questions around structured data, including databases and tabular data.

So I’m very happy to be here today, and I’m excited for our discussion.

**Amber Roberts:** Excellent! Alright. Well, Shuaichen, you mentioned you had some kind of background information that you’re going to start with, and then we can get into the paper and I guess the paper that is coming out on the next work and the applications, because I know you mentioned working in industry being interested in the applications of your research.

**Shuaichen Chang:** Yeah, sounds good. So let me give a brief introduction. Let me share my screen. 

**Amber Roberts: **And then anyone that has questions while you get that up. You could ask your questions in the chat in the Q&A. Or even in the Arize community Slack, especially if you have questions that we don’t have time for during this live session. Shuaichen’s in the Arize community Slack, and can answer those afterwards.

**Shuaichen Chang: **I’ll give about, let’s say a 5 or 10 minute introduction. But you can interrupt me if you have any questions. 

Okay, cool. So the paper is called How to Prompt LLMs for Text-to-SQL: A Study in Zero-shot, Single-Domain, and Cross-Domain Settings. We focus on the study in single domain and customer settings. So the text-to-SQL model is a component in a larger natural language interface to a structured data system. That’s pretty much what my work is about.

So basically for a system, we have a human user. The human user can interact with data by asking natural language questions. And the data in here can be like a table, relational database, or even some charts or images. And the text model is a model behind the AI agent which is able to understand the user question as well as the data and generate the appropriate response.

So to look at the detail of what a text-to-SQL model does is, it takes the natural language question, which is our “NLQ” here, as well as a relational database. So text-to-SQL model takes both of them at input and outputs a SQL query.

The SQL query will be executed against the database to obtain the final answer. So in this case the database is about players and games so questions like last name on rank of the youngest winner across all matches. So by translating this question into a SQL query, which will be executed in the database will have basically all names with the youngest winners across matches.

So in the past year or two, we have seen how fast large language models have developed in almost every application.

![LLMs for Text-to-SQL with In-context Learning](https://arize.com/wp-content/uploads/2023/12/Screenshot-2023-12-18-at-12.41.25-PM-1024x579.png)


So on the left [in this chart above] is the performance on a SQL dataset we used called Spider. We have seen some fine tuning-based models which ran on 7,000 examples. And on the right we can see the performance of some large language models with in context, learning, which means this model is not particularly trained on the training set up the data side, but just with a 0 or few shots prompting–so usually with less than 32 demonstration examples–those methods can be comparable or even better than the fine-tuning-based methods.

Those studies basically tried to enhance large models’ performance with different approaches. Some of them do retrieval. Some do intermediate reasoning stuff. They also use different strategies for constructing the prompt text of databases and demonstrations, and I will show how they did later.

So this leaves us with two slight drawbacks. One is, it’s hard to compare two works on their main contributions or prompt constructions right and a second, future work still has to explore the effective prompt constructions for the text-to-SQL task which is still called prompt engineering.

**Amber Roberts: **So, and the models that you show here, do those provide their prompt templates so that you can at least compare them like, by eye.

**Shuaichen Chang:** Yeah, yeah. So the problem is like. The prompts in general are different in every work. If they do any kind of learning. But here, I will say, the  part of the prompt will talk about  part of the contribution in their work. One is what they propose about how to retrieve demonstrations that really improve the model performance. But besides that, there’s something fundamental for every type of SQL paper is how you convert a structural database into unstructured text into the larger model, because we know that trend for predicting the next word. So they only observe a sequential input instead of a structured input. So even with a lot of work on the first part, the second part is still under study–how to basically cover the structured database into unstructured text.

**Amber Roberts: **Okay, got it. Thanks. 

**Shuaichen Chang:** So this is our focus in this paper. Our goal is to study how to represent the structure. Basically, I’m trying to say here, the structured database in the unstructured prompt. We study three common scenario. You may have questions about what the difference is between them, but we can go into that a little bit later. We also want to study how to construct the demonstration for the cross domain setting.

The zero-shot setting is the most straightforward. So imagine the model is a SQL expert. You can just give the model a database and a question, and simply expect the model to return the answer to your question given the database.So in this part, the prompt text contains the database information, including database schema and database content as well as instruction. Instruction is usually pretty simple and says what we expect the model would do given the input and the actual input questions, which is in here: how many high schoolers are there? It’s a database about high school students, I believe. And we’d expect the model to generate a SQL query that would be able to get the answer from the database.

So this is the most straightforward setting.

In this case we have a different way to represent the database information, because, how to represent the structure information into unstructured texts. So apparently the most important thing about databases is what table is there and what columns are in each table?

So this information is always necessary in almost every work. But some works also found different ways to represent some information. Besides the basic table information we have the information. The relational database contains the information in of course, multiple tables through the foreign keys, basically. So we can see all the friends in the front table, student ID is a key referring to the ID in high school. So such information can be also included in the database prompt. And, moreover, we have some other papers proposed that allows us to represent all this information in a simple table format, which is basically using a SQL query to create such a database. And this will be the input of the lateral model to represent the information in the database.

So, besides database schema, we have the database content and database content, we can include pretty much for every table with these three different rows for a table. So if we inserted more rows, using the SQL query, would that simply give us more tables? Or we propose to do that column-wise, to increase the model’s understanding of what is possible value in each column.

So, to sum up what we found in a zero-shot setting is that the type of schema is definitely always necessary, but adding the table’s relationship which is representing a foreign key, we consistently see that the model can outperform the prompt that is now using the relationship. So we showed that relationships are very helpful for the model to understand the database. Moreover, we found adding the database content to be even more beneficial. But the model doesn’t favor all ways to provide such database content.

Now let’s move to the single domain setting.

So people say: well, zero-shot settings already works so well, why do we need a single domain-setting? With single domain basically, you can imagine you have an application that you know what possible query has been asked in the past, right? So, knowing those questions that have been asked in the past will definitely have the model understand the database will know what questions are more likely to be asked in the future, and therefore it improves the understanding of future questions.

So, like the zero-shot setting, we just have one more different thing which is the demonstrations. The demonstrations are the power of questions and SQL queries this demonstration used before the test question. So we find, after having the in-domain demonstration, we find a model performance can continue enhanced when the number of in-domain demonstrations increase. So this definitely shows how powerful the demonstration is and, moreover, we find the model relies less on the table relationship when we have more examples. So remember on zero-shot with these two parallel lines [referring to chart below] there’s a gap in here, and when we have just examples, they basically merge. So the model doesn’t need that type of relationship from the database prompt, they can learn that from the in-domain examples.

![Single-domain Text-to-SQL Results](https://arize.com/wp-content/uploads/2023/12/Screenshot-2023-12-18-at-12.54.14-PM-1024x576.png)

And however we find such a domain example doesn’t provide enough information about the database content. So the larger model still would like the prompt that contains the database content directly. But by having some in domain examples, the larger model is not sensitive to the choice of prompt representation for the database content.

**Amber Roberts: **And just to clarify on the table here. So that’s the Codex language model. And using ChatGPT. This is probably a future question but have you compared this to GPT-4 or Llama II,  some of the larger models that tend to do really well with context like this and structure?

**Shuaichen Chang: **Yeah, that’s a good question. We actually determined that with some open source models which actually, now, don’t perform as well as ChatGPT. But I personally have never tried GPT-4 in this experiment–it could be pretty expensive to run this with GPT-4.

But in general my personal takeaway is that such information about the database is not something that as the model becomes more powerful, they can naturally get. They have to be exposed to the information of this specific database to perform better on those tasks.

So I believe in-domain demonstration is always necessary. Even the power, the model, can be even more powerful and developed way better in the future.

**Amber Roberts: **Okay, yeah. That makes sense. And then, in terms of the accuracy here. For how correct a query is, are you comparing like a  SQL query that you or someone on your team has written, that is correct, and runs and executes compared to the query that has been generated by this LLM, and then how do you get that 82% accuracy, for example?

**Shuaichen Chang:** Yes. So the accuracy is based on execution resolve. So we actually have a database containing a lot of rows or information inside the database. So, given a SQL query can execute a set of answer to the question. So we compare why the SQL query is correct. Then we use that query to skew that against the database to get a set of answers. We compare that with the original answer to determine whether the SQL query is correct because, you know, the same intent can be writing and SQL querying in many different ways.  

**Amber Roberts:** Yeah. But for someone that has used sequel and has almost gotten it correct. Almost gotten all the data that I need from a database. It’s interesting because I sometimes say: Well, it returned data, I must have gotten it right. But then there’s one area, or like one line that didn’t work and you just didn’t get that amount of data.

**Shuaichen Chang:** Yeah. So this actually, a pretty interesting research track just using this execution result to have the model correct yourself in a future prediction. This is not included in this work, but it’s definitely a very good direction to explore.

So then, we move to the last part of this work which is the cross-domain setting. So you may want to know what the cross-domain setting is for. So basically, you can assume that the database doesn’t come with any annotated example. In this case you can imagine the user uploading a table or relation database and another user may ask questions about it. But in this case, nobody has annotated any questions or SQL queries about the database before. And this is very similar to the zero-short setting. But a difference is people found that by using the database and an example from another domain or another database could actually enhance the model’s performance. So it’s not as good as in-domain, but it’s definitely better than zero-shot. That’s why a lot of people are exploring this direction. In this case, we construct a prompt using the demonstration.

They are corresponding to a different database than the test database. So we ideally want to answer the question better about the database on the high school database, but we can use another database. Here’s the track database, and you send a question about this database to improve the performance of the larger model on another database.

So first of all, we want to know why if it’s not providing any benefit, why don’t we just switch back to the zero-shot setting.

Compared to not using any example which gave you about 73% accuracy I can see that having some out of domain demonstration could improve the model’s performance.But in the out of domain demonstration we consider a different number of databases. Each database can come with a different number of examples.

So, the question is: given a certain number of databases we see that having more databases will first improve the performance but it sort of had a threshold for the model codex And then, after we cross this threshold, the model’s performance started to drop. So it was a little bit surprising because by having more database in the demonstration we always are a database ahead of the existing one. So if the model doesn’t like the specific demonstration, it can simply ignore that. So at least the model should be able to maintain its performance if it’s given longer context or more demonstration examples. But we find the model performance starts to drop significantly when we have more examples.

So we analyze this phenomenon and find out it’s actually related to the context lens What and how many tokens we have in the context. So for Codex, it has the maximum context lens provided by OpenAI at 8,000 and we found after the demonstration was about 5500 the performance of the model started to drop. We also experimented with ChatGPT 16K context

So the model supports 16K tokens in contact. And very just interestingly, we find a model type of similar performance. The phenomena after the contacts cause about 11K. So if you think about it. for different models, all 70% of the context is actually useful for SQL demonstration.

It could be true for other models. But I haven’t experimented with that myself. But at least for this model, or from OpenAI we see a similar trend.

**Amber Roberts:** So just the one example per database–essentially everything after that you get that improvement. But then it just kind of stops adding to the improvement as you add more and more examples?

**Shuaichen Chang:** Yeah, I believe if the model has unlimited long context, we will see this probably going up, and eventually should be similar to those lines above this one. But since the database schema is very long and has a lot of tokens, it’s very easy to let’s say we have an admissible line here very easy to cause that to make the performance drop before it actually improves more.

**Amber Roberts:** I still find that like pretty impressive compared to so that’s like  out of every  queries, still getting it correct, even with  like one example per database. Okay. That was better than my accuracy when I was first querying databases with SQL.

**Shuaichen Chang: **Yeah. But those models used a lot of training data.

**Amber Roberts:** Yeah, true.

**Shuaichen Chang:** Yeah. I think in general, after we find this in types of SQL tasks, I also found other people talk about similar phenomena in different tasks for different setting that the model may not be able to leverage the full context in different tasks. So yeah, I think it could be general. But at least in this task we find this phenomena with existing multiple models.

So now let’s back to the question we care about from the beginning, like how to construct the database prompt. So we find that the table’s relationship to the content is still important. Even with out of domain demonstration. So we can see by comparing this different part of the table, we can say it’s still better with the relationship accounts to provide the best performance even with a lot of auto domain examples.

It makes some sense to me, because, like, think about the relationship of the tables and database content. They’re very database specific. So even providing some examples from other databases, the model could leverage or understand what a relationship means. But it still has no idea about what *this *database in terms of the relationship to database content. So overall, I really hope this work can be like a handbook or something for future study, like when they want to work on types of SQL tasks with in-context learning, they don’t have to explore all different combinations of how to construct the database or how to construct schema content stuff. So we can spend less time on those things and focus on how to improve the general capability of types of SQLs for those models.

**Amber Roberts:** Yes, no, I agree with that. And then the other thing I was just going to ask, because someone in community was mentioning that they tackled a similar problem. I think this was a while ago, right when transformers and NLP was really taking off probably like around 2018 when these tasks were first becoming like, Oh, you don’t just have to write a rule based system from text to sequel. You can actually use NLP for these problems. And a lot of people thinking, oh we could get to 100% accuracy. You know, it’s pretty structured. And we’re still not there. I’m curious. What do you think is  the biggest thing blocking from that, like 90 to 100% performance?

**Shuaichen Chang: **So in my opinion. If you look at how much the in-domain example might have. I believe, like for the model–right now We’re not still not at 90. But let’s say in a few years we have GPT10 or whatever , it could possibly do pretty well like, understand the question perfect. But something is missing in what a database means. Some databases you can assume is like a wild design or wild format. So this one perfect, without any questions or anything. You understand what’s going on in the database? Right? But in industry now, a lot of databases have some, let’s say, arbitrary tokens in a column. Right? They have some, let’s say the internal knowledge to name some column or tables. In that case, since your data is private and hopefully not trained by any other models. And then why can we expect that model understand that specific database so basic cannot. So in that case, let’s say, we have a column itself like a name or grade or Id. We have a column like A, B , right? It’s random token there. So we don’t really know what’s going on in that column. So we definitely need some, for example, the in domain examples, or some explanation to that column for the model to understand.

So I feel like from 90 to 100 is not about how we input the model is about. It’s like, no human can do that without any further information. Right? So in that case, I feel like the next step is maybe how we can easily add some we call domain knowledge into the model, like by providing other give it con. Give the domain knowledge along with this database will find other way to like, say, generally, some example using a domain knowledge. So that model to understand the database better first and then answer the question about a database.

**Amber Roberts: **Okay, yeah.  That makes sense. I buy it. [Laughs] 

**Shuaichen Chang:** Well, this is actually pretty close to what we’ll be trying to do in the next one. If we have time, we can briefly talk about that?

**Amber Roberts:** Yeah, I think we have 15 min left. And yeah, pretty much all the images that you used on here were the ones I was gonna ask you about in the paper. So yeah, if you wanna go to your main paper takeaways we could talk about what you’re working on now in applications.

**Shuaichen Chang:** Yeah. But before that, do we have more questions?

**Amber Roberts:** Let’s see I think I think we got them all. Yeah, I think we got them all. I will have Sarah check in the community Slack. But from what I see from the chat, they’ve been answered in the questions that I’ve asked.

**Shuaichen Chang:** okay, cool. So basically, the next one is inspired by what makes the in-domain demonstration so useful. Right? So this is another work which is at MIT this year. So it was called “selective demonstration for customer text-to-SQL.” I personally really like the customer setting because you assume that you don’t have any example, what? What doesn’t rely on any actual annotating in-domain example. So in this case the database provider can be a non SQL expert and database user can be a non SQL expert. So basically, anyone can use the system if we create a good customer text-to-SQL model. 

But before we understand the customer, we want to understand what’s the magic part in the in-domain demonstration? So this is what we found in the Spider dataset is the same as what we talked about before. It’s another data set which also has customer text-to-SQL data. But this has a little bit more challenge than the Spider data. So we can see the zero-shot setting the codex model performed pretty good on Spider, not that good on KaggleDBQA, but having the in- domain example, kind of significant, boost the performance on both sides. So Spider from 36 to 84 and KaggleDBQA from 30 to below 70.

So we want to know what actually the in domain demonstration did here.

So the two questions we care a lot about here is first what are the key factors within the in-domain annotated example that contribute to the performance improvement. And the second is, can we harness the benefit of this in domain example without actually using the annotation?

There are three different spikes within the in-domain demonstration examples. The first is the text-to-SQL task format and knowledge, which is the general knowledge about this task. And the second is the in-domain natural language question distribution, and the last is the in-domain, SQL query distribution. So we have seen that, providing the test knowledge is pretty easy. We can just simply use the auto domain example to do that. So by having an out of domain example, we do see the performance increase in both data sets, but definitely not comparable to using the actual in-domain example. So we know. Okay, the task knowledge is beneficial, but definitely, not sufficient.

However, we do a simple play on the data. We create a mismatch, natural question and SQL queries in the demonstration. So we find a model basically could not leverage this demonstration for in-domain. So that shows us the task knowledge, even though it’s not sufficient, it’s still necessary in this task.

And then we study the in-domain NLQ and SQL distribution. So for NLQ, we use the actual natural language question, with the SQL queries that are generated by this codex model in the zero-shot setting.

In this case, the model is close to the actual natural language questions. But the SQL query is predicted by itself. So it doesn’t bring any actual knowledge. Similarly, we can give the model, say, the actual SQL query, but using the natural language that are predicted by itself. So in each setting the model is exposed to one knowledge, but not aware of the other. So we find that by having the SQL distribution, which is using the actual sequel, but predicting natural question, the model could learn almost the same as using the actual in-domain example. So it’s very close in Spider, being slightly larger in KaggleDBQA but much better than all the other settings.

So from this analysis we kind of know…maybe the SQL query about the in-domain, about a database, basically, and have the model understand something about the database. So in the future the model could answer the question better about the same database.


**Questions about the Research**

**Amber Roberts: **I have a question from our community. Member Greg, asking about: there’s been a lot of push towards vector databases. Do vector databases fit into the work that’s being done here with SQL because, we’re using a lot of relational databases compared to now, new vector databases that are being used in these large language models.

That sounds like a complicated question. I don’t know if you have thoughts about this for like where vector databases might fit in.

I think he meant using vector databases as opposed to relational databases, which I’m not sure if SQL would be used for vector databases. I don’t know if I would if they would be used together. I don’t know if you’ve come across this?

**Shuaichen Chang: **So I didn’t think about this scenario exactly, because SQL query was designed for a relational database. But for vector DB I feel like, maybe a model can do that pretty well but in a different way. The easiest way that we use the larger model is just simply give a test input right? We can definitely fine-tune that with embedding. But the easiest way for people who don’t understand AI or machine learning the way they use it is just simply just give a a natural language input in that case, the database may just easier to embed it into the larger model. Maybe we will have some larger model that are designed for like the stuff. You know, we could have the training data, the transcription models.

**Amber Roberts: **Interesting? Yeah, that’s an interesting question from community. Yeah. So getting back to these  main questions here? How do you think they’re demonstrated? So these are these the main questions that you’re trying to solve?

**Shuaichen Chang: **Yes. So we we sort of have seen the answer for the first question. I’m quickly going to the second one, how we can harness the benefit of the in-domain example.

**Amber Roberts: **Okay, perfect.

**Shuaichen Chang: **Yeah. So even though we know that okay, we found the in-domain SQL distribution is important but it’s not always available, right? You have to annotate. So first of all, you have to know what questions the user may actually ask, and annotate those questions into a SQL query, and then you can say, okay, I can use those to improve the model performance. But for, let’s say in other cases we don’t have the resources for such annotation. How can we still get the benefit? How can we leverage the funding here to create a better model?

My solution is pretty simple. So we try to sync some data about a specific database without seeing any actual examples. So here basically what we’re trying to do is we use this query. But since that example may not always be correct, especially after the query we also want to generate some natural language questions, so the questions may not be that show may not align the SQL query perfectly.

So in this case it may not provide the correct text-to-SQL knowledge. When we have seen that the correct text-to-SQL is necessary for the model. So that’s why we propose to use the hybrid source of demonstration containing both out-of-domain demonstrations. And in-domain synthetic demonstrations.

For out-of-domain, we basically tried to retrieve the out-of-domain examples that are similar to the text examples so that the language model can learn something from the out-of-domain example and use the knowledge into the test example. So we first did SQL prediction. And we used the initial SQL prediction to do the retrieval.

And for in-domain. We first need to sample the in-domain data. We sample some SQL query by using a SQL template from auto domain, example, auto domain SQL. And then we translate that SQL into our queue. And then we have a verification state which is pretty tricky. So we first translate subsequent to a natural language question, and then we translate our queue back to a SQL Query. So if the SQL query had the same execution resolved, then we can assume that the translation was correct in both directions, and then we keep this example.

So after we have the in-domain example, we do some retrieval. Similarly, we want to retrieve the example that is similar to the test question. So we maximized coverage retrieval here. We found that by using the hybrid source of demonstration, we found with our proposed framework outperformed all the baseline models as well as only using out of domain or only using in domain examples.

In general, I found the proposed methods pretty useful for multiple statistical data sets with multiple models.

**Amber Roberts:** We did get some discussion around that database. A lot of people are having to leave, because I think there’s only 60s left. But a lot of people are thanking you, Shao chien for the information. The talk. I think a lot of people have been trying to do something similar with the GPT-4 models. So one member of our community said that just by adding in a few examples in the prompt engineering really helped for a particular database that they were using to create sequel queries. So it’s great seeing more work being done this area. And then someone from community mentioned that basically he agrees with you like SQL would just not be as appropriate for a vector database because of the space relations that the relational database is built on. And how SQL inherently operates. And so that’s very interesting to see there. 

We are out of time. But thank you so much for going through your paper. Your latest results. Those are great great performance scores, and I can’t wait to see, you know, when it’s just hitting 100 every time for these examples, and I’m also interested to see how this will apply to more industry topics. But thanks everyone for joining, and I hope you all have a great rest of your week.

**Shuaichen Chang:** Yeah, thank you for having me.
