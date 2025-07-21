import pandas as pd

# Carga el archivo CSV
df = pd.read_csv('base_limpia.csv')

# Muestra las primeras filas
print("\nPrimeras filas de la base:\n")
print(df.head())

# Muestra información general de las columnas
print("\nInformación general:\n")
print(df.info())

# Muestra conteo de valores nulos por columna
print("\nValores nulos por columna:\n")
print(df.isnull().sum())

# Muestra columnas únicas
print("\nColumnas únicas:\n")
print(df.columns.tolist())

import psycopg2

conexion = psycopg2.connect(
    dbname="basedatos_colab",
    user="postgres",
    password="Dragon2307*",
    host="localhost",
    port="5432"
)

cursor = conexion.cursor()

sql = """
DROP TABLE IF EXISTS eventos_servicio;
DROP TABLE IF EXISTS servicios;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS conductores;
DROP TABLE IF EXISTS cedis;
"""

cursor.execute(sql)
conexion.commit()

print("Tablas eliminadas correctamente")

cursor.close()
conexion.close()

