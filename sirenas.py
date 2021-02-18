import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

class Sirenas:
    def __init__(self, df):
        self.df = df.copy()
        with open('logisticR.sav', 'rb') as f:
            self.model = pickle.load(f)
    def predict(self):
        return self.model.predict(self.df[['v1', 'v2', 'v3', 'v4']])
