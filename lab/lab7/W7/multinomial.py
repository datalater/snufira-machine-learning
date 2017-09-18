#################
### Logistic Regression with Sklearn
#################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, model_selection, naive_bayes, metrics, preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer


### define input data
categories = [
  'alt.atheism',
  'talk.religion.misc',
  'comp.graphics',
  'sci.space' ]

data_train = datasets.fetch_20newsgroups(subset='train', categories=categories,
                                shuffle=True, random_state=42)

data_test = datasets.fetch_20newsgroups(subset='test', categories=categories,
                               shuffle=True, random_state=42)


print(data_train.target.shape) # number of training samples
print(data_test.target.shape) # number of test samples

### parsing text files
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
X_train = vectorizer.fit_transform(data_train.data)
X_test = vectorizer.transform(data_test.data)

print(X_train.shape) # (samples, # features)

feature_names = vectorizer.get_feature_names()

# make model
# alpha: pseudocount
model = naive_bayes.MultinomialNB(alpha=0.01)

# training model
model.fit(X_train, data_train.target)

# test model
pred = model.predict(X_test)

accuracy = metrics.accuracy_score(data_test.target, pred)
