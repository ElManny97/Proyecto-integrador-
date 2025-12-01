# se plantea el analisis de lo que son las ventas de productos de la tienda, esto con la finalidad de obtener que productos on los A para generar un stock sufuciente de lo que es el producto en almacen para que no exista desabasto del producto en los proximos meses

# cargado de librerias para trabajar la infromación del proyecto
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

#carga de la información del archivo y muestrar lo que contiene
df =pd.read_csv("ventas_tienda.csv")
print("__Primeras filas de datos__")
print(df.head())
print("__Información del archivo___")
print(df.info())
print("__estadisticas generales de la ifnromación__")
print(df.describe())

#Revisión de la información y limpieza de los datos
print("__Valores faltantes por columna__")
print(df.isnull().sum())
print("valores duplicaods:\n", df.duplicated().sum())
df['fecha'] = pd.to_datetime(df['fecha'])
df["mes"] = df["fecha"].dt.month_name()
df["dia_semana"] = df['fecha'].dt.day_name()
df_limpio= df.copy()
df_limpio.drop_duplicates()
df_limpio.dropna()
print(df_limpio.dtypes)
df_limpio.sort_values("producto")
df_limpio.to_csv("ventas_tienda_limpio.csv", index=False)

print(df_limpio["producto"].unique())

#Se encontraron datos faltanates mas no se encontraron datos duplicados en el 


#Analisis descriptivo de los datos
print("__Inicio del analisis de los datos__")

#Analisis general de ventas

total_de_ventas= df_limpio["total"].sum()
promedio_de_ventas= df_limpio["total"].mean()
media_de_ventas= df_limpio["total"].median()
desviacion_estandar_de_ventas= df_limpio["total"].std()

print(f"El total de ventas es:{total_de_ventas}\n"
      f"El promedio de ventas de todos los productos: {promedio_de_ventas}\n"
      f"La media de ventas es de: {media_de_ventas}\n"
      f"La desviaicón estandar es de:{desviacion_estandar_de_ventas}")

#ya con el analisis de lo que es son las ventas vemos una mdseviaicón estandar muy grande lo cual habla de que podemos tener o una agrupación en un producto o que tenemos ventas muy erraticas

#Analisis de ventas de productos general en precio
print("__Ventas de producto__")
ventas_producto = df_limpio.groupby("producto")["total"].agg([
    ("total", "sum"),
    ("promedio", "mean")
]).sort_values("total", ascending=False)
print(ventas_producto)

#Analisis de ventas de productos general en cantidad
print("__Cantidad de productos vendidos__")
ventas_producto_cantidad = df_limpio.groupby("producto")["cantidad"].agg([
    ("cantidad", "sum"),
    ("promedio", "mean")
]).sort_values("total", ascending=False)
print(ventas_producto_cantidad)

#Analisis de ventas de productos por mes 

Ventas_de_producto_por_mes= df_limpio.groupby(["producto","mes"])["total"].sum()
Ventas_de_producto_por_mes = Ventas_de_producto_por_mes.sort_values("mes")
print(Ventas_de_producto_por_mes[["mes", "total"]])

#La idea de estos reportes e sver que productso son loq ue en venta de precio nos afectan mas y cuales en piezas son las que serian mas, lo cual nos permite ver dos cosas muy improtantes cuales son aquellos productso que pro monto aportan mas a nuestras ventas y cuales en cuestion de peizas son los que mas se mueven esta información es importante para el control de stock de la tiendas y para la paneación de pedidos de lo que es el area logistica

#graficos de ventas de productos 

plt.style.use("default")
sns.set_palette("husl")


