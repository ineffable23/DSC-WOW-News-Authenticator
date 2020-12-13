import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Read the data
df = pd.read_csv(r"C:\Users\Harshita\Downloads\\news.csv")

# Get shape and head
df.shape
df.head()

# Get the labels
labels = df.label
labels.head()

# Split the dataset
x_train, x_test, y_train, y_test = train_test_split(df['text'], labels, test_size=0.2, random_state=7)

# Initialize a TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Fit and transform train set, transform test set
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
tfidf_test = tfidf_vectorizer.transform(x_test)

# Initialize a PassiveAggressiveClassifier
pac = PassiveAggressiveClassifier(max_iter=50)
pac.fit(tfidf_train, y_train)

# Predict on the test set and calculate accuracy
y_pred = pac.predict(tfidf_test)
score = accuracy_score(y_test, y_pred)
print(f'Accuracy: {round(score * 100, 2)}%')

# Build confusion matrix
cf_matrix=confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
print(cf_matrix)

import seaborn as sns

sns.heatmap(cf_matrix/np.sum(cf_matrix), annot=True,
            fmt='.2%', cmap='Blues')


# pickle file
import pickle

# with open("pickle_pac","wb") as f:
#     pickle.dump(pac,f)
#
# with open("pickle_pac","rb") as f:
#    ppac=pickle.load(f)

pickle.dump(pac, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))