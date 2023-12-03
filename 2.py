# Nombre: Fatima Gómez Díaz
# Grupo: [951]

#Realizar una función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados

import pandas as pd
import numpy as np

def contar_renglones_duplicados(dataframe):
    duplicados = dataframe.duplicated()
    num_duplicados = duplicados.sum()

    return num_duplicados

data = {
    'Especie': ['Pez1', 'Pez2', 'Pez3', 'Pez4', 'Pez1'],
    'Temperatura': [25.0, 28.0, 25.0, 27.0, 25.0],
    'PH': [7.5, 7.2, 7.5, np.nan, 7.5],
    'Nivel_Oxigeno': [6.0, 6.0, 5.5, 6.2, 6.0]
}

acuario_df = pd.DataFrame(data)

print("DataFrame original:")
print(acuario_df)
num_duplicados = contar_renglones_duplicados(acuario_df)
print("\nNúmero de filas duplicadas:", num_duplicados)
