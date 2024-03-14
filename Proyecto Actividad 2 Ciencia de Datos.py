import requests # Importamos el paquete requests para realizar peticiones HTTP

import pandas as pd # Importamos pandas para manejar los datos

import numpy as np # Importamos numpy para realizar cálculos numéricos

import matplotlib.pyplot as plt # Importamos matplotlib para realizar los gráficos

import seaborn as sns # Importamos seaborn para graficar

import matplotlib.ticker as ticker

import plotly.express as px

# URL de la API del Banco Mundial para el PIB de El Salvador
url = "http://api.worldbank.org/v2/country/SLV/indicator/NY.GDP.MKTP.CD?date=2004:2024&format=json"

# Realizamos la petición a la API
response = requests.get(url)
if response.status_code == 200:  # Verificamos si la solicitud fue exitosa
    data = response.json()
    if len(data) > 1 and isinstance(data[1], list):
        # Convertimos los datos a un DataFrame de pandas para un análisis más fácil
        df = pd.DataFrame(data[1])
        
        # Seleccionamos las columnas de interés
        df = df[['date', 'value']]
        df.columns = ['Año', 'PIB']
        
        # Convertimos 'Año' a datetime y ordenar por esta columna
        df['Año'] = pd.to_datetime(df['Año'])
        df.sort_values('Año', inplace=True)
        
        # Calculamos el crecimiento porcentual anual del PIB
        df['Crecimiento del PIB'] = df['PIB'].pct_change() * 100
        
        # Graficamos el Crecimiento del PIB
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x='Año', y='Crecimiento del PIB')
        plt.title('Crecimiento Anual del PIB en El Salvador')
        plt.xlabel('Año')
        plt.ylabel('Crecimiento del PIB (%)')
        plt.show()
    else:
        print("No hay datos disponibles en la respuesta")
else:
    print("Fallo al obtener datos de la API del Banco Mundial")