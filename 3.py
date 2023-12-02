# Nombre: Fatima Gómez Díaz
# Grupo: [951]

import pandas as pd
import numpy as np

def eliminar_columnas_nulos(dataframe, max_porcentaje):
    # Validar que el porcentaje máximo esté entre 0 y 1
    if not (0 <= max_porcentaje <= 1):
        raise ValueError("El porcentaje máximo debe estar entre 0 y 1.")

    # Calcular el porcentaje de valores nulos por columna
    porcentaje_nulos = dataframe.isnull().mean()

    # Filtrar las columnas que superen o igualen el máximo porcentaje de valores nulos
    columnas_eliminar = porcentaje_nulos[porcentaje_nulos >= max_porcentaje].index.tolist()

    # Eliminar las columnas del DataFrame y obtener la lista de nombres de columnas eliminadas
    dataframe_modificado = dataframe.drop(columns=columnas_eliminar)
    columnas_elimindas = list(set(dataframe.columns) - set(dataframe_modificado.columns))

    return columnas_elimindas

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

# Eliminar columnas con un máximo porcentaje de valores nulos del 40%
columnas_elimindas = eliminar_columnas_nulos(acuario_df, 0.4)

# lista de columnas eliminadas
print("\nColumnas eliminadas:")
print(columnas_elimindas)
print("\nDataFrame modificado:")
print(acuario_df.drop(columns=columnas_elimindas))
