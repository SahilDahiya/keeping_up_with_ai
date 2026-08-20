---
title: Enterprise-Grade Security and Monitoring at Cresta
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: cresta
url: https://cresta.com/blog/security-and-monitoring
author: J Matt Peterson
published: '2021-03-16'
fetched: '2026-08-20T06:14:33Z'
classifier: null
taxonomy_rev: 2
words: 428
content_sha256: 294f95d2f00ade6d06872ac01713ed302f7ebb31f2dd65690676ebaaa2a98d5c
---

# Enterprise-Grade Security and Monitoring at Cresta

## **tl;dr**

Cresta has SOC-2 Type 2 security compliance with no findings. Cresta can easily create dashboards across all our customers.

### **The status quo**

Customers care about the privacy of their data and Cresta has always shared that concern as well. Customers don't just want talk, they often need proof to back up claims. Before being compliance certified, Cresta had no way to prove to outside parties our compliance posture.As part of our security posture, we create separate databases for all our customers. This makes it difficult to visualize data across all of them at the same time.

### **Cresta’s answer on security**

Cresta now has [SOC-2](https://en.wikipedia.org/wiki/System_and_Organization_Controls) Type 2 compliance. This outside validation provides a minimum bar for internal security and best practices. For Cresta, this also enables our sales organization to target larger enterprises that require compliance for external vendors.One example of our security work recently is creating a multi account AWS cloud deployment. Amazon documents these best practices [here](https://aws.amazon.com/organizations/getting-started/best-practices/), but the short version is that separating products and development environments into different accounts creates a strong security separation between them making it much harder for problems in one area to spread into another.For internal accounts, we've recently migrated to [Single Sign-On authentication](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html). Engineers do not use usernames or passwords to log into our cloud accounts. We've extended this to [EC2 instance connect](https://aws.amazon.com/blogs/compute/new-using-amazon-ec2-instance-connect-for-ssh-access-to-your-ec2-instances/) which means we also require SSO for connections to our bastion hosts or development servers.Another example of this is Cresta's use of [GitOps](https://www.weave.works/technologies/gitops/). We use GitOps to deploy application and infrastructure changes through CICD. This creates an audit trail of all system changes along with who made the change.

### **Cresta’s answer on data visualization**

Cresta uses [PrestoDB/](https://prestodb.io/)[Trino](https://trino.io/) to query and aggregate data across multiple databases in real-time. This allows us to calculate company wide results, such as KPIs, or create single use dashboards for all customers at once. It's used by internal teams to track and report on Cresta usage and report on it in Slack.[caption id="attachment_22806" align="aligncenter" width="750"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ad8b6658004d2196f_68135f270b4bb27bcd9bb622_Cresta-UAS-KPI-Dashboard-1024x373-1.avif)

A sample KPI dashboard we use to track Customer activity.[/caption][caption id="attachment_22808" align="aligncenter" width="747"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ad8b6658004d21972_68135f270b4bb27bcd9bb619_Cresta-Infra-hint-bot-1024x137-1.avif)

Cresta’s internal teams use Slack bots to track and report on Cresta usage across customers.[/caption]And it allows reuse of customer analysis through simply changing the customer name.[caption id="attachment_22810" align="aligncenter" width="750"]

![width=](https://cdn.prod.website-files.com/67feba4d16c14d85f1696c4f/68138f3ad8b6658004d21982_68135f280b4bb27bcd9bb62e_Cresta-UAS-Tools-1024x863-1.avif)

A sample output of Cresta real-time assistance visualizations.[/caption]

### **Why you should care?**

If you're a large organization with strict security compliance standards for external vendors, check out Cresta! Our suite of compliance standards is constantly growing!*Special thanks* *to the Cresta Infra squad: JMatt and Jack L.*
