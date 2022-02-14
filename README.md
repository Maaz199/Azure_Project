# Azure_Project
***Project under Future Ready Talent Internship***


# Project Synopsis
# Title: 
***Loan Approval Classification***
# Industry: 
***FinTech***
# Problem Statement/Opportunity –
Banks run into losses when a customer doesn't pay their loans on time. Because of this, every year, banks have losses in crores, and this also impacts the country's economic growth to a large extent. we will look at various attributes such as funded amount, location, loan, balance, etc., to predict if a person will be a loan defaulter or not or in other words, we can say that if bank should give out loans to a particular individual or not.
# Project Description -
This is clearly a classification ML Problem. I am going to create a model which will predict if a bank should give out loan or not. I will make a Web App where bank employee / customer with fill up the customer detail and then it will suggest whether to give loan or not. Will use automated ML in an Azure Machine Learning pipeline in Python as a backbone of this project. Will also make the endpoint of the model on Azure Kubernetes Services. 
# Primary Azure Technology: - 
- Azure Machine Learning
- Azure Kubernetes Services 
- Azure Web App
# Other Azure Technologies: 
- Compute 
- Datastore
- Azure Auto ml 
- Azure Explanation 
- Azure Container Instances  

# About Project – 
0)	**Data_Preparation.ipynb** – In this file I have done some data pre- processing for smooth process of training data by Azure Auto Ml module.
1)	**config.txt** – File containing information about azure resource group  
2)	**Loan.ipynb** – In this file I have store my data on datastore and then call it in Azure auto ml module. Also make an endpoint on Azure Container Instances for my best model from auto ml run.
3)	**Loan_approval_Cloud_Run.ipynb** – In this file I again make the end point for my best model from auto ml run in Azure container Instances but in this case, I am getting 500 error on accessing the endpoint. In the end I can’t figure out the problem so I remove the end point.
4)	**Deployement.ipynb** – In this file I created an endpoint of my best model from auto ml run on Azure Kubernetes Services and this is the end point which I am using in my Azure Web App to predict the eligibility of the loan.
5)	**\Web_App_Flask\DeployMachineLearningModels\model.py** – Checking the functionality of the endpoint on AKS and making sure everything is okay with the model deployment
6)	**\Web_App_Flask\DeployMachineLearningModels\try.py**- Checking the backend of web app making sure how we got data and how we processed it and display the results.
7)	**\Web_App_Flask\DeployMachineLearningModels\DeployFlaskAzure** – Files associated with flask app which is hosted on Azure Web App

# Screenshot of working app -
![](2022-02-09%20(1).png)

# Important links -
- ***link of YT Explaination*** - https://www.youtube.com/watch?v=mpHKGFnxKY8
- ***link of GitHub Repository*** - https://github.com/Maaz199/Azure_Project
- ***link of web app*** - http://xyzbank.azurewebsites.net/

*Actually, I also have two ml end point in this project -*
1) **Azure Container Endpoint (Can access by anyone) -**
http://1103bb47-41d4-4619-9eb8-c07e84987322.westus.azurecontainer.io/score
2) **Azure Kubernetes Service Endpoint (Need API Key to Access) -**
http://138.91.136.177:80/api/v1/service/aks-service/score


# NOTE -
I have comsumed all of my Azure Credit given to me for this project, So Web App is stopped and it is giving 403 Error. Please Bare with me.

![](2022-02-14%(1).png)

As you can see that in the Screenshot above, most of my credits is gone to Azure Kubernetes Cluster and minority of part is gone to Azure Container. I should have keep the end point to container only but it was open and anyone can access that but with Azure Kubernetes Services you need an API to access that in this eay it is more secure then container endpoint

# ***Thats all for my project*** - **Signing out Maaz Mohammed**

