import numpy as np
import pandas as pd
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

iris = sns.load_dataset("iris")
X = iris[iris.columns[:-1]]
y = iris["species"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)
model = RandomForestClassifier().fit(X_train, y_train)

with open("iris_predictor.pickle", "wb") as f:
    pickle.dump(model, f)