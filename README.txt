# PruebaTH
resultado e implementación de los ejercicios

2- Desafío para hacerla de jamón:

Para poder calificar se debe instanciar la clase regression_salchichas del módulo regresión, 
pasando como parámetro el dataframe con las variables v1, v2 y v3, que corresponden a las características de los jamones,
para obtener la calificación se debe llamar al método predict y asignarlo a la columna score del dataframe original.

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


3 - Desafío El Seductor Canto de las Sirenas
Para poder clasificar a las sirenas se debe instanciar la clase Sirenas del modulo sirenas,
pasando como parámetro el dataframe con las variables v1, v2, v3 y v4 que corresponden a las características de las sirenas,
para obtener la clasificación se debe llamar al método predict y asignarlo a la columna especie del dataframe original.

import sirenas
import pandas as pd

sirenas_clasif = pd.read_csv("sirenas_endemicas_y_sirenas_migrantes.csv")

model = sirenas.Sirenas(sirenas_clasif)
sirenas_clasif['especie'] = model.predict()

print(sirenas_clasif.head(2))
