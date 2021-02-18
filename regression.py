import pickle
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

class regression_salchichas:
    def __init__(self, df):
        with open("ls_best.sav", 'rb') as f:
            self.cols = pickle.load(f)
        with open("scaler_X.sav", 'rb') as f:
            self.scaler_X = pickle.load(f)
        with open("scaler_y.sav", 'rb') as f:
            self.scaler_y = pickle.load(f)
        with open("model_mlp.sav", 'rb') as f:
            self.model = pickle.load(f)
        self.df = self.poly_(df)
        
    def poly_(self,df):
        df = df.copy()
        for i in ['v1','v2','v3']:
            df[f"p2_{i}"] = np.power(df[i],2)
            df[f"p3_{i}"] = np.power(df[i],3)
            df[f"p4_{i}"] = np.power(df[i],4)
        return df.copy()

    def predict(self):
        X = pd.DataFrame(self.scaler_X.transform(self.df[self.cols]), columns=self.cols)
        return np.round(self.scaler_y.inverse_transform(self.model.predict(X)),0)
