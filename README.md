# PruebaTH
resultado e implementación de los ejercicios

Desafío para hacerla de jamón:

Para poder calificar se debe instanciar la clase regression_salchichas del módulo regresión
pasando como parámetro el dataframe con las variables v1, v2 y v3, para obtener la calificación se debe llamar
al método predict y asignarlo a la columna score del dataframe original.

NOTA: Se ocupan los archivos .sav donde se encuentra guardados los modelos y variables. 
ls_best.sav 
model_mlp.sav 
scaler_X.sav 
scaler_y.sav 

import regression
import pandas as pd

calificar = pd.read_csv("jamones_por_calificar.csv")

reg = regression.regression_salchichas(calificar)
calificar['score'] = reg.predict()

print(calificar.head(2))
