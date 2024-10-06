# Ejercicio 1. Mediante teclado especificar los siguiente:
# - Numero de columnas que tendrá el dataframe
# - Una vez que se especifique, preguntar por los datos que tendra esa Serie
# - Preguntar por los nombres de las columnas que tendrá el dataframe
# - Preguntar por los nombres de las filas que tendrá el dataframe
# - Una vez introducidos los datos, crear el dataframe que contenga esa información
# - Mostrar el dataframe


import pandas as pd
num_col = int(input("Introduce el número de columnas que tendrá el dataframe: "))
data = []
for i in range(num_col):
    col_data = input(f"Introduce los datos de la columna {i + 1}, separados por comas: ").split(",")
    data.append(col_data)

col_names = input("Introduce los nombres de las columnas, separados por comas: ").split(",")
row_names = input("Introduce los nombres de las filas, separados por comas: ").split(",")
df = pd.DataFrame(data=data, index=row_names).T  # .T para transponer los datos
print("\nDataFrame resultante:")
print(df)