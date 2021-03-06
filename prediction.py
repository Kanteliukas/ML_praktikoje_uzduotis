import numpy as np
import pandas as pd
import seaborn as sns
import pickle

with open("iris_predictor.pickle", "rb") as f:
    pickle_model = pickle.load(f)

def make_prediction(sl, sw, pl, pw):
    sl = float(sl)
    sw = float(sw)
    pl = float(pl)
    pw = float(pw)
    prediction = pickle_model.predict([[sl, sw, pl, pw]])
    return prediction[0]