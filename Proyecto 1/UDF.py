import sqlite3
import pandas as pd

square = lambda n : n*n

with sqlite3.connect("Northwind.db") as conn: # Se establece conexion con DB la conexión se cierra automaticamente
    conn.create_function("square", 1, square) # Creas la función en SQL, el primer parametro es el nombre de la función en SQL , el segundo es cuantos parametros pide la función y el tercero es la función en python
    cursor = conn.cursor() # cursor es un elemento que permite realizar consultar y entregarlas de vuelta
    cursor.execute('''
        SELECT *,square(Price) as Precio_al_cuadrado FROM Products
        WHERE Price > 0
        ''') # Ejecuta una consulta de SQL y comienza una transacción
    results = cursor.fetchall() # Obtiene la información, en tuplas
    results_df = pd.DataFrame(results) # Lo convertimos a forma de tabla
    
print(results_df)
