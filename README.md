# DSC-WOW-News-Authenticator

This is a Machine Learning Project made by team Neophytes (313) for Code Off Duty by DSC WOW.

## Problem Statement of this project:

Fake news spreads like a wildfire and this is a big issue nowadays. We need learn how to distinguish fake news from a real one. We can use supervised learning to implement a model like this.

## Objective of this project:

We made this project in python with objective to build a model to accurately classify a piece of news as REAL or FAKE.

## Working of this project:

This python project of news authenticator deals with fake news and real news. Using sklearn (scikit), we build a TfidfVisualizer on our dataset. Then, we initialize a PassiveAgressive Classifier and fit the model. In the end, the accuracy score and the confusion matrix tell us how well our model fares.

## Brief explaination of this project:

### Fake News
 Fake news is a type of yellow journalism that encapsulates pieces of news that may be hoaxes and is generally spread through social media and other online media. This is often done to impose certain ideas and is often achieved with political agendas. Such news items may contain false and/or exaggerated claims, and may end up being viralized by algorithms, and users may end up in a filter bubble.

### TfidfVectorizer

#### TF (Term Frequency):

The number of times a word appears in a document is its Term Frequency. A higher value means a term appears more often than others, and so, the document is a good match when the term is part of the search terms.

#### IDF (Inverse Document Frequency):

Words that occur many times a document, but also occur many times in many others, may be irrelevant. IDF is a measure of how significant a term is in the entire corpus.

The TfidfVectorizer converts a collection of raw documents into a matrix of TF-IDF features.

### PassiveAggressiveClassifier

Passive Aggressive algorithms are online learning algorithms. Such an algorithm remains passive for a correct classification outcome, and turns aggressive in the event of a miscalculation, updating and adjusting. Unlike most other algorithms, it does not converge. Its purpose is to make updates that correct the loss, causing very little change in the norm of the weight vector.

### Dataset

The dataset we've used for this python project is news.csv. This dataset has a shape of 7796x4. The first column identifies the news, the second and third are the title and text, and the fourth column has labels denoting whether the news is REAL or FAKE.

### Steps for detecting fake news with Python
#### 1. Make necessary imports:
![Image of Step 1](C:\Users\Harshita\Pictures)

## Contributors of this project:

### 1. Harshita Verma (ineffable23)

- [LinkedIn ](https://www.linkedin.com/in/harshita-verma-528132178)

### 2. Vamsi Pyla (VAMSIPYLA)

- [LinkedIn ](https://www.linkedin.com/in/vamsi-pyla-0885771a1)


We are currently working on this part of the project. We'll update this soon.

Thanks for visiting!!!!


