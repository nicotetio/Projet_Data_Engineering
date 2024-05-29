import json
import os
import pandas as pd
from joblib import dump
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score,precision_score,recall_score

MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)

print("Loading dataset...")
reviewDataCleaned = pd.read_csv('reviewDataCleaned.csv')

print("splitting the data")
independent_var = reviewDataCleaned.cleaned_review
dependant_var = reviewDataCleaned.sentiment
X_train, X_test, y_train, y_test = train_test_split(independent_var, dependant_var, test_size=0.20, random_state=0)

#Define TfidfVectorizer
vectorizerTF = TfidfVectorizer()

#Define classifier
clf2 = LogisticRegression(solver='lbfgs')

#Pipeline vectorizer and then classifier
clf = Pipeline([('vectorizer', vectorizerTF), ('classifier', clf2)])

print("fitting model")
clf.fit(X_train, y_train)

#computing meta data
predictions = clf.predict(X_test)
accuracy = accuracy_score(predictions, y_test)
precision = precision_score(predictions, y_test, average='weighted')
Recall = recall_score(predictions, y_test, average='weighted')
metadata = {
	'accuracy_score' : accuracy,
	'precision_score' : precision,
	'recall_score' : Recall
	}
	
print("Serializing model to: {}".format(MODEL_PATH))
dump(clf, MODEL_PATH)

print("Saving metadata to: {}".format(METADATA_PATH))
with open(METADATA_PATH, 'w') as output:
	json.dump(metadata, output)

