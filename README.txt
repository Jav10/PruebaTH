# PruebaTH
resultado e implementación de los ejercicios

1- Desafío Aguas Venenosas

Para poder obtener las Aguas que podrían estar envenenadas, se necesita instanciar la clase Veneno del módulo veneno,
pasando como parámetro el número de aguas que se requiera investigar y llamar al método csv, esto generará un archivo
csv con los identificadores de las aguas.

El orden en el que están ordenadas (de arriba para abajo) las aguas indica el nivel de atención que se les debe dar.

NOTA: Se ocupa el archivo .sav donde se encuentra guardado el modelo.
distance.sav

import veneno
import pandas as pd


dist = veneno.Veneno(50)
dist.csv()

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

NOTA: Se ocupa el archivo .sav donde se encuentra guardado el modelos.
logisticR.sav

import sirenas
import pandas as pd

sirenas_clasif = pd.read_csv("sirenas_endemicas_y_sirenas_migrantes.csv")

model = sirenas.Sirenas(sirenas_clasif)
sirenas_clasif['especie'] = model.predict()

print(sirenas_clasif.head(2))
