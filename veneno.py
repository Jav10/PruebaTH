import pickle
import pandas as pd

class Veneno:
    def __init__(self, num):
        with open('distance.sav', 'rb') as f:
            self.distance = pickle.load(f)
        self.num = num
    
    def csv(self):
        s = pd.Series(self.distance.loc[self.distance.index!=9999,9999].sort_values().head(self.num).index)
        s.to_csv("urgente_orden_de_cierre.csv", index=False)
