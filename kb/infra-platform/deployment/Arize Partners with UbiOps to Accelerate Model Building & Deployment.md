---
title: Arize Partners with UbiOps to Accelerate Model Building & Deployment
topic: infra-platform
subtopic: deployment
secondary_topics:
- industry/announcements
summary: Partnership announcement with UbiOps focused on connecting model building,
  deployment, and observability workflows.
source: arize
url: https://arize.com/blog/arize-partners-with-ubiops/
author: Krystal Kirkland
published: '2021-06-07'
fetched: '2026-07-11T04:42:35Z'
classifier: codex
taxonomy_rev: 1
words: 899
content_sha256: 8ee96b7befffb0adabddb2ea50ed8955ec996baff6748f13a7b3a233443f45bd
---

# Arize Partners with UbiOps to Accelerate Model Building & Deployment

![Group-496-1024x573](https://arize.com/wp-content/uploads/2021/06/Group-496-1024x573-1-1021x560.png)

              # Arize Partners with UbiOps to Accelerate Model Building & Deployment

*Written in collaboration with UbiOps.*

**UbiOps and Arize**

UbiOps is the easy-to-use serving and hosting layer for data science code. UbiOps stands out for its ease of use, freedom to write any code you want while eliminating the need for in-depth IT knowledge. It is a serving, hosting and management layer on top of your preferred infrastructure. Accessible via the UI, client library, or CLI, it’s suitable for every type of data scientist.

UbiOps is specifically useful for real-time applications that require both simple processing scripts or complex ML models. Thanks to the scalable infrastructure every piece of code can be scaled up and down according to your specifications.

Arize allows for real time observability of machine learning models. Arize extends beyond traditional monitoring and is uniquely focused on enabling ML engineers with a comprehensive observability platform to more effectively detect and troubleshoot issues, perform analysis, and improve model performance.

The platform is backed by an evaluation store, which allows teams to connect datasets across training, validation and production environments. By storing performance metrics for each model version in an evaluation store, users can leverage any dataset as a baseline reference to monitor and explain model performance in production. The evaluation store can hook into an existing feature store and model store to create a virtuous feedback loop for model improvements.

**Why this integration?**

The more business-critical a model is, the more important observability is to keep a pulse on its health and to quickly resolve any issues that arise.

While deployment of a production-worthy AI model poses a challenge to many, observability is another, deeper challenge that awaits a model in production. With this integration, data scientists and ML engineers can work together to develop a model, push it to production, and gain full visibility and control of its performance.

Teams using Arize and UbiOps together are able to:

- Validate model quality and performance prior to deploying to production.
- Accelerate model deployment (time to value) and iterations without high ops overhead.
- Automatically diagnose issues that emerge in production, with ability to analyze specific cohorts of problematic predictions.
- Gain deeper visibility into how models are performing with features such as performance heatmaps, and find opportunities to deliver improvements / retraining.

![](https://arize.com/wp-content/uploads/2021/06/ubiops_arize.png)

**1. Integration walkthrough and instructions**

To demonstrate how Arize and UbiOps can work together we’ll use a (locally trained) TensorFlow model that predicts the miles per gallon usage of a car based on specific attributes such as the amount of cylinders, horsepower, weight and model year.

We’ll work in a jupyter notebook and make use of the UbiOps client libraries to communicate with the backend to host and serve the code. The full notebook can be found [here](https://docs.arize.com/arize/integrations/integrations/ubiops). The below code snippets show how UbiOps and Arize integrate.

This code block is the deployment.py file that UbiOps uses to deploy models on its platform. When new data is sent in, it goes through the request function in order for the model to make predictions. In this example, we send in both the input feature data and the actual data to this function, making it the perfect place to place our Arize logging code. We simply use Arize’s bulk_log method, passing in features, predictions, actuals, and optional prediction timestamps, and just like that we have our model logged and ready to explore on the Arize platform.

```
class Deployment:
   def __init__(self, base_directory, context):
       model_file = os.path.join(base_directory, "tensorflow_model.h5")
       self.model = load_model(model_file)
       self.arize = Client(organization_key=os.environ.get('ARIZE_ORGANIZATION_KEY'), api_key=os.environ.get('ARIZE_API_KEY'))
   def request(self, data):
       input_data = pd.read_csv(data['data'])
       actuals = input_data.pop('MPG')
       prediction = self.model.predict(input_data)
       ########### ARIZE CODE HERE ###########
       ids = pd.DataFrame(input_data.index.values).applymap(str)
       # OPTIONAL: Simulate predictions evenly distributed over 30 days by manually specifying prediction time
       current_time = datetime.datetime.now().timestamp()
       earlier_time = (datetime.datetime.now() - datetime.timedelta(days=30)).timestamp()
       optional_prediction_timestamps = np.linspace(earlier_time, current_time, num=len(ids))
       optional_prediction_timestamps = pd.Series(optional_prediction_timestamps.astype(int))

       responses = self.arize.bulk_log(
           model_id="arize-ubiops-tutorial",
           model_type=ModelTypes.NUMERIC,
           model_version="v1",
           prediction_ids= ids,
           prediction_labels=pd.DataFrame(prediction),
           prediction_timestamps=optional_prediction_timestamps,
           actual_labels=actuals,
           features=input_data)
       #######################################
       # Writing the prediction to a csv for further use
       print('Writing prediction to csv')
       pd.DataFrame(prediction).to_csv('prediction.csv', header = ['MPG'], index_label= 'index')
       return {
           "prediction": 'prediction.csv',
       }
```
**2. Example end result visualised in Arize **

#### Here’s an example of how Arize visualises model performance in production, with data coming in on a daily basis. The platform provides a snapshot of the overall health of a model, surfacing key metrics such as accuracy, false positive rate, recall, amongst others (see fig. 2). Moreover, the current performance distributions can be compared against training, validation or historical performance baselines (see fig. 3).

Arize Performance Dashboard

![](https://arize.com/wp-content/uploads/2021/06/arize-dashboard-300x201.png)

Arize PSI Monitor

![](https://arize.com/wp-content/uploads/2021/06/arize-PSI-monitor-300x162.png)

This example shows how one can simply deploy, in a fully scalable (containerised) environment, a TensorFlow model that is directly available for high frequency requests. In this case, anyone that likes to see what the expected MPG is of a car, can receive the results in a matter of seconds. This is ideal for example a webapp providing such a service. What’s more, with Arize’s monitoring functionality you can keep track of the model’s performance, automatically monitor it and conduct pre-launch validations to ensure a successful launch of your project.

Using the provided integration notebook you can deploy and monitor your own model quickly. The full notebook can be found [here](https://docs.arize.com/arize/integrations/integrations/ubiops).

If you have questions, remarks or suggestions, please don’t hesitate to contact Ubiops via their [Slack channel](https://join.slack.com/t/ubiops-community/shared_invite/zt-np02blts-5xyFK0azBOuhJzdRSYwM_w) or get in touch with Arize via their [Community on Slack](https://join.slack.com/t/arize-ai/shared_invite/zt-h3t7afis-5AuUGzDjTRpdDijiWv3jWA).
