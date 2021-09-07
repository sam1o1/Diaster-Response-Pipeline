# Disaster Response Pipeline
![Flask_app](https://github.com/sam1o1/Diaster-Response-Pipeline/blob/main/disaster-response-pipeline/screenshots/Img1.png?raw=true)
## Table of Content:

 - [Project Overview](#overview)
 -  [Installation](#installation)
 - [File Descriptions](#files)
 - [Get Started](#get_start)
 - [Licensing  and Authors](#L&A)
 - [Classification Example](#example)
  
<a name="overview"></a>
## Project Overview 
In this project, ETL and machine learning pipelines are used to build a model based on the  [Figure Eight](https://www.figure-eight.com/) dataset to classify disaster messages so that the messages can be sent  to an appropriate disaster relief agency. The user can type the disaster message and the message will get classified and the result category will displayed for him.  
<a name="installation"></a>
## Installation
In order to run this project you need to install:
 - [`Plotly 2.0.1`](https://plotly.com/)
 - [`Flask 5.3.1`](https://flask.palletsprojects.com/en/2.0.x/)
 - [`sqlalchemy`](https://www.sqlalchemy.org/)
 - [`nltk`](https://www.nltk.org/)

<a name="files"></a>
## File Descriptions

 1. Data
    * `disaster_categories.csv` : The categories dataset 
    * `disaster_messages.csv` : The messages dataset
    * `process_data.py` : the python script that includes Pipleines for loading , cleaning , merging the two datasets and storing them in Sqllite database. 
 2. Models 
	* `train_classifier.py` : NLP pipeline that tokenizes, lemmatizes, and normalizes the database generated from the `process_data.py`  ML pipleline that trains and evaluates a machine learning model on the data set after splitting it into training and test sets. 
	*  The `classifer.pkl` is saved from the ML pipeline 
3. App : The flask app used to deploy the model
4. Screenshots of the web app 
5. Jupyter Notebooks
	* `ETL Pipeline Preparation` For testing and building the ETL and  data processing pipeline
	* `ML Pipeline Preparation` For building the NLP, ML pipeline and choose the best parameters.  
 ## Get Started
 <a name="get_start"></a>
Use the following command to download the files : 

    git clone https://github.com/sam1o1/Diaster-Response-Pipeline.git
Run the following python command to generate the db:

    python process_data.py disaster_messages.csv disaster_categories.csv DisasterResponse.db
Build and train the ML model using:

    python train_classifier.py ../data/DisasterResponse.db classifier.pkl
Finally run the flask app

    python run.py
<a name="example"></a>
## Classification Example
<p> This an example of using the Flask Web app to classify a message </p>


![example](https://github.com/sam1o1/Diaster-Response-Pipeline/blob/main/disaster-response-pipeline/screenshots/img3.png?raw=true)



<a name="L&A"></a>
## Licensing  and Authors


Author : Eslam Abdelghany 

Email: eslam322_1@hotmail.com

[License](https://github.com/sam1o1/Diaster-Response-Pipeline/blob/main/LICENSE)

 
 

