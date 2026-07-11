---
title: Eight Takeaways From The Industry’s Largest Event On Machine Learning Observability
topic: industry
subtopic: trends
secondary_topics:
- evals-observability/monitoring
summary: Event recap summarizing major themes from a machine-learning observability
  gathering.
source: arize
url: https://arize.com/blog/eight-takeaways-from-the-industrys-largest-event-on-machine-learning-observability/
author: David Burch
published: '2022-04-08'
fetched: '2026-07-11T04:44:43Z'
classifier: codex
taxonomy_rev: 1
words: 1622
content_sha256: d3264994e11af80d9d932af7b00460542ab384b721bcdd0550f42acb0402c5a0
---

# Eight Takeaways From The Industry’s Largest Event On Machine Learning Observability

![arize-observe-cover](https://arize.com/wp-content/uploads/2022/04/arize-observe-cover-1021x560.png)

              # Eight Takeaways From The Industry’s Largest Event On Machine Learning Observability

Arize:Observe, an annual summit focused on machine learning (ML) observability, wrapped up last week before an audience of over 1,000 technical leaders and practitioners. Now [available for on-demand streaming](https://arize.com/ao22/), the event features multiple tracks and talks from Etsy, Kaggle, Opendoor, Spotify, Uber and many more. Here are a few highlights and quotes from some of the top sessions. Watch all of them [here](https://arize.com/ao22/).

## Keynote: Arize Goes Self-Serve

In the keynote, Arize’s co-founders – CEO Jason Lopatecki and Chief Product Officer Aparna Dhinakaran – announced that Arize’s ML observability platform is also now available on a self-serve basis, including a free version! [Sign up here](https://app.arize.com/auth/join).

“The reality today is that most teams are only doing ‘red light; green light’ model monitoring and haven’t yet embraced true [ML observability](https://arize.com/ml-observability/) with [ML performance tracing](https://arize.com/blog/machine-learning-performance-tracing/) to pinpoint the source of model performance problems before they impact customers or the bottom line,” said Arize Co-Founder and Chief Product Officer Aparna Dhinakaran. “We are changing that with a platform that is purpose-built to tackle the toughest ML observability challenges of the world’s most respected organizations. Customers of all sizes are now able to try, buy and deploy our AI model monitoring capabilities and expand their model coverage as their needs change.”

## Scaling A Machine Learning Platform Is All About the Customer

In the “[Scaling Your ML Practice](https://www.youtube.com/watch?v=jX4EKexpZUM)” panel, Coinbase’s Director of Engineering Chintan Turakhia puts it bluntly: “a platform for one is not a platform.” His advice to teams looking to build from the ground up: “don’t talk about the ML platform first; talk about what problems you’re solving for your customers and how you can make the business better with ML…Doing ML for ML’s sake is great and there are whole worlds like Kaggle that are built for that, but solving a core customer problem” is everything in making the case internally, he argues.

## Machine Learning Infrastructure Is More Complex Than Software Infrastructure

In the “[ML Platform Power Builders: Assemble!](https://www.youtube.com/watch?v=it364HJ1Woc)” panel, Smitha Shyam, Director of Engineering at Uber, makes an important distinction between machine learning infrastructure and software and data infrastructure.

“There is a misconception that ML is all about the algorithms,” she says. “In reality machine learning is data, systems, and the model. So the infrastructure that’s required to support machine learning from the initial development to deployment to the ongoing maintenance is very large and complex. There are also dependences on the underlying data layers in the system in which these models operate. As an example, seemingly innocent changes in the data layer can completely change the model output. Unlike software engineering, the ML job is not done when you’ve just tested your model and put it in production — model predictions change as data changes, market conditions change, you have seasonality, and your surrounding systems and business assumptions change. You have to account for all of these things as you’re building the entire ML platform infrastructure.”

As a result, ML infrastructure is “a superset of what goes into your software infrastructure, data infrastructure, and then things that are unique to modeling itself,” she continues.

## Diversity Is Table Stakes

Shawn Ramirez, PhD, Head of Data Science at Shelf Engine — where women hold 50% of all leadership positions — is quick to point out the myriad benefits of diversity at her company. “I think commitment to diversity and inclusion at Shelf Engine matters in so many ways,” she says. “First, it affects the accuracy and bias in our data science models. Second, it changes the development of our product. And finally, it impacts the quality of and retention in our team.”

Tulsee Doshi, Head of Product – Responsible AI and Human-Centered Technology at Google, adds that it’s important to not overlook the global dimensions of diversity. “A lot of what we talk about in the press today is very Western-centric – we’re talking about failure modes that are related to communities in the United States – but I think a lot of these concerns around fairness, around systemic racism and bias, actually differ pretty significantly when you go to different regions,” she says.

## AI Ethics Is About Much More Than Compliance or Explainability

According to a broad cross-section of speakers, having an AI ethics strategy in place is also critical for enterprises. “Responsible AI is not an addition to your data science practice, it’s not a luxury item to be added to your operations, it’s something that needs to be there from day one,” notes Bahar Sateli, Senior Manager of AI and Analytics at PwC.

To Reid Blackman, Founder and CEO of Virtue Consultants, it’s also something that starts at the top. “One of the reasons we’re not seeing as much AI ethics in practice as we ought to is a lack of senior leadership,” he says. Ultimately, AI ethics needs to be “woven through how you think about financial incentives for employees, how you think about roles and responsibilities,” he adds.

For many, new approaches for AI ethics risk management are needed. “We can’t avoid the fact that models will make mistakes and we need to have the right guardrails and accountability for that,” notes Tulsee Doshi of Google. “But we can also do a lot to pre-empt possible mistakes if we are careful in the metrics that we develop and are really intentional about making sure that we are slicing those metrics in different ways, that we’re developing a diversity of metrics to measure different types of outcomes.” She cautions on over-reliance on explainability or transparency in that process: “I don’t think either of those is by itself a solution to AI ethics concerns in the same way that a single metric is not a solution…these things work in concert together.”

## The Data-Centric AI Revolution Heightens The Need For End-To-End Observability

In the “[Bracing Yourself For a World of Data-Centric AI](https://www.youtube.com/watch?v=jfK_YO5mmFE)” panel, Diego Oppenheimer, Executive Vice President of DataRobot, notes that the worlds of citizen data scientists and specialized data science teams have some commonalities. “The operations change, but the part that is consistent – and this is interesting – is as the use cases multiply and as you have more people participating in the development of machine learning models and applying ML to use cases, the rigor around security, scale, governance, and understanding what’s going on and audibility and observability across the stack becomes even more important because you have sprawl — which…is only a bad thing if you don’t know what’s happening,” he notes.

Michael Del Balso, CEO and co-founder of Tecton, also notes the importance of insight across the ML lifecycle. “The teams that build really high quality ML applications” manage well across the ML flywheel, he explains. “It’s not just about the learn phase, not just the deciding phase – they’re also thinking about, say, how does my data get back from my application into a training dataset? They’re playing in all parts of that cycle and…making it much faster.”

## The Machine Learning Infrastructure Space Is Maturing

Many speakers marvel at how far the industry has come in such a short time. As Josh Baer, Machine Learning Platform Product Lead at Spotify, points out: “when we started out, there weren’t a lot of solutions out there that addressed our needs that we had as options to buy so we had to build a lot of the basic components ourselves.”

Anthony Goldbloom, CEO and founder of Kaggle, concurs: “some of the tooling — including Arize — is really starting to mature in helping to deploy models and have confidence that they are doing what they should be doing.”

## 🔮The Future: Multimodal Machine Learning

In the “[Embedding Usage and Visualization In Modern ML Systems](https://www.youtube.com/watch?v=Q506BR2aaV4)” panel, Leland McInnes, the creator of UMAP and a researcher at the Tutte Institute for Mathematics and Computing, lays out what he is excited about as the future unfolds. On the more theoretical side, McInnes notes that “there’s a lot of work on sheaves and cellular sheaves which is a very abstruse mathematical thing but turns out to be surprisingly useful” with “a lot of relations to graph neural networks” that are beginning to show up in the literature.

On UMAP in particular, McInnes says the “vastly underused” [parametric UMAP](https://timsainburg.com/parametric-umap.html) merits closer attention. He is also “very interested in how to align different UMAP models. There is an aligned UMAP that can align data that you can explicitly define a relationship with one dataset to another, but what if I just start with two arbitrary datasets — say, word vectors from French and word vectors from English and no dictionary? How do you produce a UMAP embedding that aligns those so I can embed both? There are ways to do that,” he says, with “Grumov Wasserstein distance” as a key search term for those interested in learning more. “People are going to align all these different multimodal datasets via these sorts of techniques,” he says.

Kaggle’s Goldbloom is equally excited about this space. “Some of the possibilities around multimodal ML are an area for excitement,” he says, particularly “multimodal training. Say you’re trying to do speech recognition where you can hear what is being said — what if you can include a camera to lip-read at the same time?”

## Conclusion

With global enterprise investment in AI systems [expected](https://www.wsj.com/articles/retail-set-to-overtake-banking-in-ai-spending-11631007001) to eclipse $200 billion by 2023, it’s an exciting time for the future of the industry. It’s also an important time for ML teams to learn best practices from peers and make foundational investments in ML platforms – including ML observability with ML performance tracing – to navigate a world where model issues directly impact business results.
