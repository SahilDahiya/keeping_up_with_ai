---
title: Shipping NLP Sentiment Classification Models With Confidence
topic: evals-observability
subtopic: monitoring
secondary_topics: []
summary: Shows how to monitor NLP sentiment classification models in production, with
  attention to data and prediction drift.
source: arize
url: https://arize.com/blog/nlp-sentiment-classification-monitoring/
author: Francisco Castillo
published: '2022-09-15'
fetched: '2026-07-11T04:45:52Z'
classifier: codex
taxonomy_rev: 1
words: 2249
content_sha256: 5ddc37ba003a8def18e2b3d032e5581d96e49c076af36698f90db8eacfb1fd0c
---

# Shipping NLP Sentiment Classification Models With Confidence

![NLP cover image nlp sentiment classification monitoring](https://arize.com/wp-content/uploads/2022/09/NLP-cover-image-1021x560.jpg)

              # Shipping NLP Sentiment Classification Models With Confidence

#### This code-along walkthrough covers how to ingest embedding data and look at embedding drift. You can follow along the Colab version of this blog [here](https://colab.research.google.com/github/Arize-ai/tutorials_python/blob/main/Arize_Tutorials/Embeddings/NLP/Arize_Tutorial_NLP_Sentiment_Classification_HuggingFace.ipynb).

*This blog was written in partnership with  Nate Mar, Founding Engineer at Arize*

Increasingly, companies are turning to natural language processing (NLP) sentiment classification to better understand and improve customer experience. From call centers to loyalty programs, these models inform important business decisions across a [wide](https://arize.com/blog/rise-of-the-ml-engineer-elizabeth-hutton-cisco/) [variety](https://arize.com/resource/sharechat-grows-engagement/) of customer touch-points. Unfortunately, most ML teams lack reliable ways to monitor these models in production. To help, Arize debuted new capabilities for [monitoring unstructured data](https://arize.com/blog/monitor-unstructured-data-with-arize/) earlier this year. This guide is designed to help you get started.

Let’s say you are in charge of maintaining a sentiment classification model. This simple model takes online reviews of products from your U.S.-based store as the input and predicts whether the reviewer’s sentiment is positive, negative, or neutral. You trained your sentiment classification model on English reviews. However, once the model was released into production, your colleagues start to notice that the performance of the model has degraded over a period of time.

Arize is able to surface the reason for this performance degradation. In this example, a sudden influx of reviews written in Spanish impact the model’s performance. You can surface and troubleshoot this issue by analyzing the embedding vectors associated with the online review text.

It is worth noting that, according to our research, inspecting embedding drift can surface problems with your data before it causes performance degradation.

Sound interesting? This blog covers how to start from scratch. We will:

- Download the data
- Preprocess the data
- Train the model
- Extract embedding vectors and predictions
- Log the inferences into the Arize Platform

We will be using 🤗 Hugging Face’s open source libraries to make this process extremely easy. In particular, we will use:

- 🤗 [Datasets](https://huggingface.co/docs/datasets/index): a library for easily accessing and sharing datasets and evaluation metrics for Natural Language Processing (NLP), computer vision, and audio tasks.
- 🤗 [Transformers](https://huggingface.co/docs/transformers/index): a library to easily download and use state-of-the-art pre-trained models. Using pre-trained models can lower your compute costs, reduce your carbon footprint, and save you time from training a model from scratch.

If this is your first time using Arize, we recommend [signing up for a free account](https://app.arize.com/auth/join) and [sending data to Arize](https://colab.research.google.com/github/Arize-ai/client_python/blob/main/arize/examples/tutorials/Arize_Tutorials/Quick_Start/Send_data_to_Arize_in_5_easy_steps_classification.ipynb) in five easy steps before continuing. If you are familiar with sending data to Arize, it only takes a few more lines to send embedding data. Let’s get started!

## Step 0: Setup and Getting the Data

The preliminary step is to install 🤗 Hugging Face’s datasets and transformers libraries, mentioned above. In addition, we will import some metrics from **scikit-learn***.*

We’ll explain each of the imports below as we use them.

### Install Dependencies and Import Libraries 📚

### Check if GPU Is Available

### 🌐 Download the Data

The easiest way to load a dataset is from the Hugging Face Hub. There are already thousands of datasets in over 100 languages on the Hub. At Arize, we have crafted the [arize-ai/ecommerce_reviews_with_language_drift](https://huggingface.co/datasets/arize-ai/ecommerce_reviews_with_language_drift) dataset for this example notebook.

Thanks to Hugging Face 🤗 datasets, we can download the dataset in one line of code. The Dataset object comes equipped with methods that make it very easy to inspect, pre-process, and post-process your data.


### Inspect the Data

It is often convenient to convert a * Dataset* object to a Pandas

**so we can access high-level APIs for data visualization. 🤗 Datasets provides a**

*DataFrame***method that allows us to change the output format of the Dataset. This does not change the underlying data format, an Arrow table. When the**

*set_format()***format is no longer needed, we can reset the output format using**

*DataFrame***.**

*reset_format()*`train_ds.set_format("pandas")`

display(train_ds[:].head())

train_ds.reset_format()

## Step 1: Developing Your Sentiment Classification Model

### Pre-Processing the Data

Before being able to input the data into the model for fine-tuning, we need to perform an important step: [tokenization](https://arize.com/blog-course/tokenization/).

Transformer models like ** DistilBERT** cannot receive raw strings as input. We need to

*tokenize*and

*encode*the text as numerical vectors. We will perform

*Subword Tokenization*, which is learned from the pre-training corpus. Its goal is to allow tokenization of complex words (or misspellings) into smaller units that the model can learn, and keep common words as unique entities, keeping the length of the input to a reasonable size.

🤗 Transformers provides the AutoTokenizer class, which allows us to quickly download the tokenizer required by the pre-trained model of our choosing.

In this case, we will use the following checkpoint: ** distilbert-base-uncased**.

`model_ckpt = "distilbert-base-uncased"`

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

Next, let’s define a processing function to tokenize the examples in the dataset. The ** padding** and

**options are added to keep the inputs to a consistent length. Shorter sequences are padded and longer ones are truncated. We can apply said processing function to entire dataset objects by using the**

*truncation***method.**

*map()*Two columns have appeared in each dataset:

- *input_ids*
- *attention_mask*

We can display the dataset changes as it was shown above:

`train_ds.set_format("pandas")`

display(train_ds[:].head())

train_ds.reset_format()

### Build the Model

Similar to how we obtained the tokenizer, 🤗 Transformers provides the ** AutoModelForSequenceClassification** class, which allows us to quickly download a pre-trained transformer model with a classification

[task head](https://huggingface.co/course/en/chapter2/2?fw=pt#model-heads-making-sense-out-of-numbers)on top. The pre-trained model to use in this tutorial is

[DistilBERT](https://huggingface.co/distilbert-base-uncased). The weights of the classification task head will be randomly initialized.

It is important to pass ** output_hidden_states = True** to be able to compute the embedding vectors associated with the text (explained below). First, let’s download the pre-trained model.

We then use the ** TrainingArugments** class to define the training parameters. This class stores a lot of information and gives you control over the training and evaluation.

Next, define a metrics calculation function to evaluate the model.

Finally, fine-tune the model using the ** Trainer** class.

## Step 2: Post-Processing Your Data

Here, we will extract the prediction labels and the text embedding vectors. The latter are formed from the hidden states of the pre-trained (and then fine-tuned) model.

## Step 3: Prepare Your Data To Be Sent To Arize

From this point forward, it is convenient to use Pandas DataFrames. This can be done easily using the format methods already covered.

`train_df = train_ds.to_pandas()`

val_df = val_ds.to_pandas()

prod_df = prod_ds.to_pandas()

#### Update the Timestamps

The data that you are working with was constructed in April of 2022. Hence, we will update the timestamps so they are current at the time that you’re sending data to Arize.

#### Map Labels To Class Names

We want to log the inferences with the corresponding class names (for predictions and actuals) instead of the numeric label. Since we used 🤗 Datasets to download the dataset, it came equipped with methods to do this.

The dataset we downloaded defined the label to be an instance of the ** datasets.ClassLabel** class, which has the convenient method

**(visit Hugging Face**

*int2str*[documentation](https://huggingface.co/docs/datasets/v2.2.1/en/package_reference/main_classes#datasets.ClassLabel.names)for more information).

#### Add Prediction IDs

The Arize platform uses prediction IDs to link a prediction to an actual. [Visit the Arize documentation](https://docs.arize.com/arize/sending-data/model-schema-reference#5.-prediction-id) for more details. You can generate prediction IDs as follows:

## Step 4: Sending Data Into Arize 💫

The first step is to setup the Arize client. After that we will log the data.

#### Import and Setup Arize Client

Copy the Arize ** API_KEY** and

**from your Space Settings page (shown below) to the variables in the cell below. We will also be setting up some metadata to use across all logging.**

*SPACE_KEY*![space settings](https://arize.com/wp-content/uploads/2022/09/space-settings.png)


Now that our Arize client is setup, let’s go ahead and log all of our data to the platform. For more details on how ** arize.pandas.logger** works, visit

[our documentation](https://docs.arize.com/arize/data-ingestion/api-reference/python-sdk/arize.pandas).

#### Define the Schema

A Schema instance specifies the column names for corresponding data in the DataFrame. While we could define different Schemas for training and production datasets, the DataFrames have the same column names, so the Schema will be the same in this instance.

To ingest non-embedding features, it suffices to provide a list of column names that contain the features in our DataFrame. Embedding features, however, are a little bit different.

Arize allows you to ingest not only the embedding vector, but the raw data associated with that embedding, or a URL link to that raw data. Therefore, up to three columns can be associated to the same embedding object*. To be able to do this, Arize’s SDK provides the ** EmbeddingColumnNames** class, used below.

**NOTE:* This is how we refer to the 3 possible pieces of information that can be sent as embedding objects:

- Embedding *vector*
- Embedding *data*
- Embedding **link_to_data**

Learn more [here](https://docs.arize.com/arize/model-types/natural-language-processing-nlp#nlp-classification-model-schema-parameters).

#### Log Data

## Step 5: Confirm Data Is In Arize and Get Started ✅

Note that the Arize platform takes about 15 minutes to index embedding data. While the model should appear immediately, the data will not show up until the indexing is complete. Feel free to head over to the **Data Ingestion** tab for your model to watch Arize works its magic!🔮

You will be able to see the predictions, actuals, and feature importances that have been sent in the last 30 minutes, day, or week.

An example view of the Data Ingestion tab from a model, when data is sent continuously over 30 minutes, is shown in the image below.

![data ingestion with arize tab](https://arize.com/wp-content/uploads/2022/09/data-ingestion-arize.png)


#### Check the Embedding Data in Arize

First, set the baseline to the training set that was logged before.

![check baseline nlp sentiment classification model](https://arize.com/wp-content/uploads/2022/09/check-baseline-arize-nlp-sentiment-classification.gif)


If your model contains embedding data, you will see it in your Model Overview page.

![model overview page](https://arize.com/wp-content/uploads/2022/09/model-overview-page-arize-nlp-sentiment-classification.png)


Click on the Embedding Name or the Euclidean Distance value to see how your embedding data is drifting over time. In the picture below, Arize represents the global euclidean distance between your production set (at different points in time) and the baseline (which we set to be our training set). We can see there is a period of a week where suddenly the distance is remarkably higher. This shows that during that time text data sent to our model that was different than what it was trained on (English). This is the period of time when reviews written in Spanish were sent alongside the expected English reviews.

![](https://arize.com/wp-content/uploads/2022/09/embedding-drift-nlp-sentiment-classification.png)


In addition to the drift tracking plot, you can also find the Uniform Manifold Approximation and Projection (UMAP) visualization of your data in Arize under the point in time selected. Notice that the production data and our baseline (training) data are superimposed, which is indicative that the model is seeing data in production similar to the data it was trained on.

![umap nlp sentiment classification](https://arize.com/wp-content/uploads/2022/09/umap-nlp-sentiment-classification.jpg)


Next, select a point in time when the drift was high and select a UMAP visualization in two dimensions (2D). We can see that both training and production data are superimposed for the most part, but another cluster of production data has appeared. This indicates that the model is seeing data in production qualitatively different to the data it was trained on, and in this case causing performance degradation.

![new cluster umap](https://arize.com/wp-content/uploads/2022/09/new-cluster-umap-production-data-arize-embedding-monitoring.png)


For further inspection, select a three-dimensional (3D) UMAP view and click Explore UMAP to expand the view. With this view, you can interact in 3D with the dataset. Zoom, rotate, and drag to see the areas of the dataset that are most interesting.

![umap visualization of nlp sentiment classification model](https://arize.com/wp-content/uploads/2022/09/explore-umap-3d-monitor-nlp-sentiment-classification.gif)


In the UMAP display, Arize offers many coloring options:

- **By Dataset:**The coloring distinguishes between production data versus baseline data (training in this example). This is specifically useful to detect drift. In this example, we can see that there is some production data far away from any training data, giving an indication of severe dataset drift. We can identify exactly what datapoints our baseline is missing so that re-train effectively.
- **By Prediction Label:**This coloring option gives an insight on how a model is making decisions. Where are the different classes located in the space? Is the model predicting one class in regions where it should be predicting another?
- **By Actual Label:**This coloring option is great for identifying labeling issues. If other colors are visible inside an orange cloud, for instance, it is a good idea to check and see if the labels are wrong. Further, we can use the corrected labels for re-training.
- **By Correctness:**This coloring option offers a quick way of identifying where the bulk of your model’s mistakes are placed, giving you an area to pay attention to. In this example, we can see that the Spanish reviews are almost all red.
- **By Confusion Matrix:**This coloring option allows you to select a positive class and color the data-points as True Positives, True Negatives, False Positives, False Negatives.

More coloring options will be added to help understand and debug your model and dataset, including color by feature values.

#### Final Note

If you want to remove this example model from your account, just click *Models -> NLP-reviews-demo-language-drift -> config -> delete*

## Wrapping Up 🎁

As teams deploy more NLP sentiment classification models into production, having monitoring in place to track embedding drift and root cause issues that arise is critical for staying ahead of potential performance degradation in the real world.

By completing this guide, your team should now have an easier and more automated way to tackle these challenges head-on!

Questions? Reach out on the [Arize community](https://arize.com/community/). For additional Colabs, check out the [Arize Docs](https://docs.arize.com/arize/tracing-and-troubleshooting/7.-troubleshoot-embedding-data).
