# Nombre: Fatima Gómez Díaz
# Grupo: [951]

#Realizar una función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena. La cadena solo puede ser mean, bfill o ffill, en caso contrario lanzar una excepción. Debe sustituir los valores nulos por el método especificado y retornar el DataFrame modificado.

import pandas as pd
import numpy as np

def remplazar_nulos(dataframe, columnas, metodo):
    if metodo not in ['mean', 'bfill', 'ffill']:
        raise ValueError("El método debe ser 'mean', 'bfill' o 'ffill'.")

    columnas_invalidas = set(columnas) - set(dataframe.columns)
    if columnas_invalidas:
        raise ValueError(f"Las siguientes columnas no existen en el DataFrame: {', '.join(columnas_invalidas)}.")

    for columna in columnas:
        if metodo == 'mean':
            dataframe[columna].fillna(dataframe[columna].mean(), inplace=True)
        elif metodo == 'bfill':
            dataframe[columna].fillna(method='bfill', inplace=True)
        elif metodo == 'ffill':
            dataframe[columna].fillna(method='ffill', inplace=True)

    return dataframe

data = {
    'Especie': ['Pez1', 'Pez2', 'Pez3', 'Pez4', 'Pez5'],
    'Temperatura': [25.0, 28.0, np.nan, 27.0, np.nan],
    'PH': [7.5, 7.2, 6.8, np.nan, 7.0],
    'Nivel_Oxigeno': [6.0, np.nan, 5.5, 6.2, 5.8]
}

acuario_df = pd.DataFrame(data)

print("DataFrame original:")
print(acuario_df)

acuario_df_modificado = remplazar_nulos(acuario_df, ['Temperatura', 'PH'], 'mean')
print("\nDataFrame modificado:")
print(acuario_df_modificado)
