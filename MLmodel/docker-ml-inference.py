import pandas as pd
import os
import csv
from joblib import load
from sklearn.model_selection import train_test_split

MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE = os.environ["MODEL_FILE"]
METADATA_FILE = os.environ["METADATA_FILE"]
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)
METADATA_PATH = os.path.join(MODEL_DIR, METADATA_FILE)

print("Loading dataset...")
reviewDataCleaned = pd.read_csv('reviewDataCleaned.csv')

independent_var = reviewDataCleaned.cleaned_review
dependant_var = reviewDataCleaned.sentiment
X_train, X_test, y_train, y_test = train_test_split(independent_var, dependant_var, test_size=0.20, random_state=0)

#
#####################################################################################################
# Load model
print("Loading model from: {}".format(MODEL_PATH))
clf = load(MODEL_PATH)

#
#####################################################################################################
# Run inference
print("Scoring observations...")
y_predict = clf.predict(X_test)
print(y_predict)

