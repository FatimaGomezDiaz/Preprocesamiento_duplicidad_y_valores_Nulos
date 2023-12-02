# Nombre: Fatima Gómez Díaz
# Grupo: [951]

import pandas as pd
import numpy as np

def porcentaje_nulos_por_columna(dataframe):
    porcentaje_nulos = (dataframe.isnull().mean() * 100).round(2)
    return porcentaje_nulos

data = {
    'Especie': ['Pez1', 'Pez2', 'Pez3', 'Pez4', 'Pez5'],
    'Temperatura': [25.0, 28.0, np.nan, 27.0, np.nan],
    'PH': [7.5, 7.2, 6.8, np.nan, 7.0],
    'Nivel_Oxigeno': [6.0, np.nan, 5.5, 6.2, 5.8],
    'Iluminacion': [12, 14, 15, np.nan, 13],
    'Peso': [30.0, 35.0, 32.0, np.nan, np.nan]
}

acuario_df = pd.DataFrame(data)

print("DataFrame original:")
print(acuario_df)

porcentaje_nulos_columnas = porcentaje_nulos_por_columna(acuario_df)
print("\nPorcentaje de valores nulos por columna:")
print(porcentaje_nulos_columnas)
