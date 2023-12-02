# Nombre: Fatima Gómez Díaz
# Grupo: [951]

import pandas as pd
import numpy as np

def eliminar_renglones_duplicados(dataframe):
    num_duplicados_originales = dataframe.duplicated().sum()
    dataframe_modificado = dataframe.drop_duplicates()
    num_duplicados_nuevos = dataframe_modificado.duplicated().sum()
    renglones_eliminados = num_duplicados_originales - num_duplicados_nuevos
    return renglones_eliminados

data = {
    'Especie': ['Pez1', 'Pez2', 'Pez3', 'Pez4', 'Pez1'],
    'Temperatura': [25.0, 28.0, 25.0, 27.0, 25.0],
    'PH': [7.5, 7.2, 7.5, np.nan, 7.5],
    'Nivel_Oxigeno': [6.0, 6.0, 5.5, 6.2, 6.0]
}

acuario_df = pd.DataFrame(data)
print("DataFrame original:")
print(acuario_df)

renglones_eliminados = eliminar_renglones_duplicados(acuario_df)
print("\nCantidad de renglones eliminados:", renglones_eliminados)
print("\nDataFrame modificado:")
print(acuario_df.drop_duplicates())
